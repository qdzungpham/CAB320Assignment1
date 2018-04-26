# -*- coding: utf-8 -*-
"""
Created on  Feb 27 2018

@author: frederic

Scaffholding code for CAB320 Assignment One

This is the only file that you have to modify and submit for the assignment.

"""

import numpy as np

import itertools

import generic_search

from assignment_one import (TetrisPart, AssemblyProblem, offset_range, 
#                            display_state, 
                            make_state_canonical, play_solution, 
#                            load_state, make_random_state
                            )

# ---------------------------------------------------------------------------

def print_the_team():
    '''
    Print details of the members of your team 
    (full name + student number)
    '''
    
    
    #raise NotImplementedError

    print('Rick Pham, 09579249')
#    print('Grace Hopper, 12340002')
#    print('Maryam Mirzakhani, 12340003')
    
# ---------------------------------------------------------------------------
        
def appear_as_subpart(some_part, goal_part):
    '''    
    Determine whether the part 'some_part' appears in another part 'goal_part'.
    
    Formally, we say that 'some_part' appears in another part 'goal_part',
    when the matrix representation 'S' of 'some_part' is a a submatrix 'M' of
    the matrix representation 'G' of 'goal_part' and the following constraints
    are satisfied:
        for all indices i,j
            S[i,j] == 0 or S[i,j] == M[i,j]
            
    During an assembly sequence that does not use rotations, any part present 
    on the workbench has to appear somewhere in a goal part!
    
    @param
        some_part: a tuple representation of a tetris part
        goal_part: a tuple representation of another tetris part
        
    @return
        True if 'some_part' appears in 'goal_part'
        False otherwise    
    '''
    
    #raise NotImplementedError

    #    a = np.array(some_part)  # HINT
    
    S = np.array(some_part)
    G = np.array(goal_part)
    
    S_max_row = S.shape[0]
    S_max_col = S.shape[1]
    
    G_max_row = G.shape[0]
    G_max_col = G.shape[1]
    
    for row in range(0, G_max_row - S_max_row + 1):
        for col in range(0, G_max_col - S_max_col + 1):
            M = G[row:row+S_max_row,col:col+S_max_col]
            
            is_appeared_as_subpart = ((S==0)|(S==M)).all()
            
            if is_appeared_as_subpart:
                return True
            
    return False


# ---------------------------------------------------------------------------
        
def cost_rotated_subpart(some_part, goal_part):
    '''    
    Determine whether the part 'some_part' appears in another part 'goal_part'
    as a rotated subpart. If yes, return the number of 'rotate90' needed, if 
    no return 'np.inf'
    
    The definition of appearance is the same as in the function 
    'appear_as_subpart'.
                   
    @param
        some_part: a tuple representation of a tetris part
        goal_part: a tuple representation of another tetris part
    
    @return
        the number of rotation needed to see 'some_part' appear in 'goal_part'
        np.inf  if no rotated version of 'some_part' appear in 'goal_part'
    
    '''
    
    #raise NotImplementedError
    if appear_as_subpart(some_part, goal_part):
        return 0
    
    tetris_part = np.array(some_part)
    
    for num_rotation in range(1, 4):
        tetris_part = np.array(tetris_part[:,::-1]).transpose()
        if appear_as_subpart(tetris_part, goal_part):
            return num_rotation
    
    return np.inf
    
# ---------------------------------------------------------------------------

class AssemblyProblem_1(AssemblyProblem):
    '''
    
    Subclass of 'assignment_one.AssemblyProblem'
    
    * The part rotation action is not available for AssemblyProblem_1 *

    The 'actions' method of this class simply generates
    the list of all legal actions. The 'actions' method of this class does 
    *NOT* filtered out actions that are doomed to fail. In other words, 
    no pruning is done in the 'actions' method of this class.
        
    '''

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        # Call the parent class constructor.
        # Here the parent class is 'AssemblyProblem' 
        # which itself is derived from 'generic_search.Problem'
        super(AssemblyProblem_1, self).__init__(initial, goal, use_rotation=False)
    
    def actions(self, state):
        """
        Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once.
        
        @param
          state : a state of an assembly problem.
        
        @return 
           the list of all legal drop actions available in the 
            state passed as argument.
        
        """
        #

        #raise NotImplementedError

        # part_list = list(state)  #    HINT
        
        part_list = list(state)       
        
        all_legal_actions = []
        
        for pa_index in range(len(part_list)):
            for pu_index in range(len(part_list)):
                if pa_index != pu_index:
                    start, end = offset_range(part_list[pa_index], part_list[pu_index])
                    for offset in range(start, end):
                        all_legal_actions.append((part_list[pa_index], part_list[pu_index], offset))
        
        return all_legal_actions
        


    def result(self, state, action):
        """
        Return the state (as a tuple of parts in canonical order)
        that results from executing the given
        action in the given state. The action must be one of
        self.actions(state).
        
        @return
          a state in canonical order
        
        """
        # Here a workbench state is a frozenset of parts        
 
        #raise NotImplementedError

        # pa, pu, offset = action # HINT
        
        part_list = list(state)
        
        pa, pu, offset = action

        part_list.remove(pa)
        part_list.remove(pu)
        
        new_part = TetrisPart(pa, pu, offset)
        
        
        part_list.append(new_part.get_frozen())
        
        return make_state_canonical(part_list)

# ---------------------------------------------------------------------------

class AssemblyProblem_2(AssemblyProblem_1):
    '''
    
    Subclass of 'assignment_one.AssemblyProblem'
        
    * Like for AssemblyProblem_1,  the part rotation action is not available 
       for AssemblyProblem_2 *

    The 'actions' method of this class  generates a list of legal actions. 
    But pruning is performed by detecting some doomed actions and 
    filtering them out.  That is, some actions that are doomed to 
    fail are not returned. In this class, pruning is performed while 
    generating the legal actions.
    However, if an action 'a' is not doomed to fail, it has to be returned. 
    In other words, if there exists a sequence of actions solution starting 
    with 'a', then 'a' has to be returned.
        
    '''

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        # Call the parent class constructor.
        # Here the parent class is 'AssemblyProblem' 
        # which itself is derived from 'generic_search.Problem'
        super(AssemblyProblem_2, self).__init__(initial, goal)
    
    def actions(self, state):
        """
        Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once.
        
        A candidate action is eliminated if and only if the new part 
        it creates does not appear in the goal state.
        """
        #

        #raise NotImplementedError
        
        part_list = list(state)       
        
        filtered_actions = []
        
        for pa_index in range(len(part_list)):
            for pu_index in range(len(part_list)):
                if pa_index != pu_index:
                    start, end = offset_range(part_list[pa_index], part_list[pu_index])
                    for offset in range(start, end):
                        new_part = TetrisPart(part_list[pa_index], part_list[pu_index], offset)
                        if new_part.offset != None:
                            if appear_as_subpart(new_part.get_frozen(), self.goal[0]):
                                filtered_actions.append((part_list[pa_index], part_list[pu_index], offset))
        
        return filtered_actions


# ---------------------------------------------------------------------------

class AssemblyProblem_3(AssemblyProblem_1):
    '''
    
    Subclass 'assignment_one.AssemblyProblem'
    
    * The part rotation action is available for AssemblyProblem_3 *

    The 'actions' method of this class simply generates
    the list of all legal actions including rotation. 
    The 'actions' method of this class does 
    *NOT* filter out actions that are doomed to fail. In other words, 
    no pruning is done in this method.
        
    '''

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        # Call the parent class constructor.
        # Here the parent class is 'AssemblyProblem' 
        # which itself is derived from 'generic_search.Problem'
        super(AssemblyProblem_3, self).__init__(initial, goal)
        self.use_rotation = True

    
    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once.
        
        Rotations are allowed, but no filtering out the actions that 
        lead to doomed states.
        
        """
        #

        #raise NotImplementedError
        
        part_list = list(state)       
        
        all_legal_actions = []
        
        for pa_index in range(len(part_list)):
            all_legal_actions.append((part_list[pa_index], None, None))
            for pu_index in range(len(part_list)):
                if pa_index != pu_index:
                    start, end = offset_range(part_list[pa_index], part_list[pu_index])
                    for offset in range(start, end):
                        all_legal_actions.append((part_list[pa_index], part_list[pu_index], offset))
        
        return all_legal_actions

        
    def result(self, state, action):
        """
        Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state).

        The action can be a drop or rotation.        
        """
        # Here a workbench state is a frozenset of parts        
 
        #raise NotImplementedError
        
        part_list = list(state)

        pa, pu, offset = action
        
        if pu == None:
            part_list.remove(pa)
            
            rotated_part = TetrisPart(pa)
            rotated_part.rotate90()
            
            part_list.append(rotated_part.get_frozen())
            
            return make_state_canonical(part_list)
        else:
            part_list.remove(pa)
            part_list.remove(pu)
        
            new_part = TetrisPart(pa, pu, offset)
        
        
            part_list.append(new_part.get_frozen())

            return make_state_canonical(part_list)
        
        
# ---------------------------------------------------------------------------

class AssemblyProblem_4(AssemblyProblem_3):
    '''
    
    Subclass 'assignment_one.AssemblyProblem3'
    
    * Like for its parent class AssemblyProblem_3, 
      the part rotation action is available for AssemblyProblem_4  *

    AssemblyProblem_4 introduces a simple heuristic function and uses
    action filtering.
    See the details in the methods 'self.actions()' and 'self.h()'.
    
    '''

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        # Call the parent class constructor.
        # Here the parent class is 'AssemblyProblem' 
        # which itself is derived from 'generic_search.Problem'
        super(AssemblyProblem_4, self).__init__(initial, goal)

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once.
        
        Filter out actions (drops and rotations) that are doomed to fail 
        using the function 'cost_rotated_subpart'.
        A candidate action is eliminated if and only if the new part 
        it creates does not appear in the goal state.
        This should  be checked with the function "cost_rotated_subpart()'.
                
        """

        #raise NotImplementedError
        
        part_list = list(state)       
        
        filtered_actions = []
    
        
        for pa_index in range(len(part_list)):
            filtered_actions.append((part_list[pa_index], None, None))
            for pu_index in range(len(part_list)):
                if pa_index != pu_index:
                    start, end = offset_range(part_list[pa_index], part_list[pu_index])
                    for offset in range(start, end):
                        new_part = TetrisPart(part_list[pa_index], part_list[pu_index], offset)
                        if new_part.offset != None:
                            if appear_as_subpart(new_part.get_frozen(), self.goal[0]):
                                filtered_actions.append((part_list[pa_index], part_list[pu_index], offset))
        
        return filtered_actions
        
        
    def h(self, n):
        '''
        This heuristic computes the following cost; 
        
           Let 'k_n' be the number of parts of the state associated to node 'n'
           and 'k_g' be the number of parts of the goal state.
          
        The cost function h(n) must return 
            k_n - k_g + max ("cost of the rotations")  
        where the list of cost of the rotations is computed over the parts in 
        the state 'n.state' according to 'cost_rotated_subpart'.
        
        
        @param
          n : node of a search tree
          
        '''

        #raise NotImplementedError
        n_part_list = list(n.state)
        
        k_n = len(n_part_list)
        
        k_g = len(self.goal)
        
        max_num_rotations = 0
        
        for i in range(k_n):
            num_rotations = cost_rotated_subpart(n_part_list[i], self.goal[0])
            if num_rotations > max_num_rotations:
                max_num_rotations = num_rotations
        
        return k_n - k_g + max_num_rotations

# ---------------------------------------------------------------------------
        
def solve_1(initial, goal):
    '''
    Solve a problem of type AssemblyProblem_1
    
    The implementation has to 
    - use an instance of the class AssemblyProblem_1
    - make a call to an appropriate functions of the 'generic_search" library
    
    @return
        - the string 'no solution' if the problem is not solvable
        - otherwise return the sequence of actions to go from state
        'initial' to state 'goal'
    
    '''

    print('\n++  busy searching in solve_1() ...  ++\n')
    #raise NotImplementedError
    
    # assembly_problem = AssemblyProblem_1(initial, goal) # HINT
    assembly_problem = AssemblyProblem_1(initial, goal)
    
    solution_node = generic_search.breadth_first_graph_search(assembly_problem);
    
    if solution_node == None:
        return "no solution"
    else:
        return solution_node.solution()
    

# ---------------------------------------------------------------------------
        
def solve_2(initial, goal):
    '''
    Solve a problem of type AssemblyProblem_2
    
    The implementation has to 
    - use an instance of the class AssemblyProblem_2
    - make a call to an appropriate functions of the 'generic_search" library
    
    @return
        - the string 'no solution' if the problem is not solvable
        - otherwise return the sequence of actions to go from state
        'initial' to state 'goal'
    
    '''

    print('\n++  busy searching in solve_2() ...  ++\n')
    #raise NotImplementedError

    assembly_problem = AssemblyProblem_2(initial, goal)
    
    solution_node = generic_search.breadth_first_graph_search(assembly_problem);
    
    if solution_node == None:
        return "no solution"
    else:
        return solution_node.solution()
    

# ---------------------------------------------------------------------------
        
def solve_3(initial, goal):
    '''
    Solve a problem of type AssemblyProblem_3
    
    The implementation has to 
    - use an instance of the class AssemblyProblem_3
    - make a call to an appropriate functions of the 'generic_search" library
    
    @return
        - the string 'no solution' if the problem is not solvable
        - otherwise return the sequence of actions to go from state
        'initial' to state 'goal'
    
    '''

    print('\n++  busy searching in solve_3() ...  ++\n')
    #raise NotImplementedError
    
    assembly_problem = AssemblyProblem_3(initial, goal)
    
    solution_node = generic_search.breadth_first_graph_search(assembly_problem);
    
    if solution_node == None:
        return "no solution"
    else:
        return solution_node.solution()
    
# ---------------------------------------------------------------------------
        
def solve_4(initial, goal):
    '''
    Solve a problem of type AssemblyProblem_4
    
    The implementation has to 
    - use an instance of the class AssemblyProblem_4
    - make a call to an appropriate functions of the 'generic_search" library
    
    @return
        - the string 'no solution' if the problem is not solvable
        - otherwise return the sequence of actions to go from state
        'initial' to state 'goal'
    
    '''

    #         raise NotImplementedError
    print('\n++  busy searching in solve_4() ...  ++\n')
    #raise NotImplementedError
    
    assembly_problem = AssemblyProblem_4(initial, goal)
    
    solution_node = generic_search.astar_graph_search(assembly_problem);
    
    if solution_node == None:
        return "no solution"
    else:
        return solution_node.solution()
        
# ---------------------------------------------------------------------------


    
if __name__ == '__main__':
    pass
    
