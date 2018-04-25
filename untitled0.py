# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 10:51:53 2018

@author: PQD
"""
import numpy as np

from assignment_one import (TetrisPart, AssemblyProblem, offset_range, display_state, 
                            make_state_canonical, play_solution, 
                            load_state, make_random_state)

from my_solver import (appear_as_subpart, 
                       cost_rotated_subpart,
                       AssemblyProblem_1, solve_1,
                       AssemblyProblem_2, solve_2,
                       AssemblyProblem_3, solve_3,
                       AssemblyProblem_4, solve_4
                       )

def test():
    pa_1 =   ( (0, 2),
             (0, 2),
             (1, 1))
    pa_2 =   ( (0, 2),
             (0, 2),
             (1, 1))
    
    pb =   ((9, 9, 9, 9, 9, 0, 0, 0),
            (0, 0, 0, 0, 1, 2, 2, 2),
            (0, 0, 0, 0, 1, 0, 2, 0),
            (0, 0, 1, 1, 1, 1, 2, 0),
            (0, 0, 0, 1, 0, 1, 1, 0))
    
    A = np.array(pa_1)
    B = np.array(pa_2)
    C = np.array(pb)
    
    r = (A==0)
    w = (A==B)
    
    #print(r)
    #print(w)
    
    #print((r | w).all())
    max_row = 3
    max_col = 2
    
    g_max_row = 5
    g_max_col = 8
    
    for row in range(0, g_max_row - max_row + 1):
        for col in range(0, g_max_col - max_col + 1):
            q = C[row:row+max_row,col:col+max_col]
            print(q)
    
    #q = C[1:3,0:3]
    
    #print(q)
    
def test2():
    a =   ( (0, 2),
            (0, 2),
            (1, 1))
    #self.part = np.array(self.part[:,::-1]).transpose()
    #b = np.array(a[:,::-1])
    b= np.array(a)
    print(b)
    c = np.array(b[:,::-1]).transpose()
    print(c)
    d = np.array(c[:,::-1]).transpose()
    print(d)
    
def actions(state):
        
        part_list = list(state)       
        
        legal_actions = []
        
        for pa_index in range(len(part_list)):
            for pu_index in range(len(part_list)):
                if pa_index != pu_index:
                    start, end = offset_range(part_list[pa_index], part_list[pu_index])
                    for offset in range(start, end):
                        legal_actions.append((part_list[pa_index], part_list[pu_index], offset))
        
        return legal_actions
    
def result(state, action):

        
        part_list = list(state)
        
        pa, pu, offset = action

        part_list.remove(pa)
        part_list.remove(pu)
        
        new_part = TetrisPart(pa, pu, offset)
        
        part_list.append(new_part.get_frozen())
        
        return make_state_canonical(part_list)

def test_solve1():
    initial_state = load_state('workbenches/wb_05_i.txt')        
       

    goal_state_yes = load_state('workbenches/wb_05_g.txt')  
    
    La_yes = solve_1(initial_state,goal_state_yes)
    
    print(La_yes)
    
def test_solve2():
    initial_state = load_state('workbenches/wb_05_i.txt')        
       

    goal_state_yes = load_state('workbenches/wb_05_g.txt')  

    La_yes = solve_2(initial_state,goal_state_yes)
    
    print(La_yes)
    
def test3():
    
    initial_state = load_state('workbenches/wb_09_i.txt')
    c = initial_state[0]
    print(initial_state)
    print(c)
    d= TetrisPart(c)
    d.rotate90()
    print(d.get_frozen())
    display_state((d.get_frozen(),c))
    
def test4():
    a0 =   ( (2, 2, 1),
            (0, 0, 1))
    
    a1 =   ( (0, 2),
            (0, 2),
            (1, 1))
    a2 =   ( (1, 0, 0),
            (1, 2, 2))
    
    a3 =   ( (1, 1),
            (2, 0),
            (2, 0))
    
    a4 =   ( (2, 2),
            (0, 2),
            (1, 1))
    
    b =   ( (0, 2, 2, 1),
            (1, 0, 0, 1),
            (1, 1, 1, 1))
    
    print(cost_rotated_subpart(a4, b))
    
if __name__ == '__main__':
    test4()

    
    
    
    
    
    