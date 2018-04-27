

'''

A few functions to do some basic test on  your submission (file 'my_solver.py')

** Note that the markers will use many other examples to assess your code **



'''
import time

import random

from assignment_one import (TetrisPart, AssemblyProblem, offset_range, display_state, 
                            make_state_canonical, play_solution, 
                            load_state, make_random_state)

from my_solver import (appear_as_subpart, 
                       AssemblyProblem_1, solve_1,
                       AssemblyProblem_2, solve_2,
                       AssemblyProblem_3, solve_3,
                       AssemblyProblem_4, solve_4
                       )


# ---------------------------------------------------------------------------

def test_appear_as_subpart():
    '''
    Test 'appear_as_subpart' function on some examples
    
    '''

    # no
    pa_1 =   ( (2, 2, 2),
             (0, 3, 0),
             (1, 2, 0))
    # yes
    pa_2 =   ( (2, 2, 2),
             (0, 2, 0),
             (1, 2, 0))

    # yes
    pa_3 =   ( (0, 2),
             (0, 2),
             (1, 1))

    pb =   ((9, 9, 9, 9, 9, 0, 0, 0),
   (0, 0, 0, 0, 1, 2, 2, 2),
   (0, 0, 0, 0, 1, 0, 2, 0),
   (0, 0, 1, 1, 1, 1, 2, 0),
   (0, 0, 0, 1, 0, 1, 1, 0))
    
#    pprint.pprint(pa)
#    pprint.pprint(pb)

    ta_1 = TetrisPart(pa_1) 
    ta_2 = TetrisPart(pa_2) 
    ta_3 = TetrisPart(pa_3) 
    tb = TetrisPart(pb)
    tb.display('\nPart b')
    ta_1.display('\nSubpart of part b?  No')
    ta_2.display('\nSubpart of part b?  Yes')
    ta_3.display('\nSubpart of part b?  Yes')

    test_passed =  (  
            appear_as_subpart(pa_2,pb)
            and 
            appear_as_subpart(pa_3,pb)
            and 
            not  appear_as_subpart(pa_1,pb)            
            )
    
    return test_passed

# ---------------------------------------------------------------------------

def test_solve_1():
    '''
    Test function  'my_solver.solve_1'
    '''

    initial_state = load_state('workbenches/wb_05_i.txt')        
    goal_state_no = load_state('workbenches/wb_01_i.txt')        

    goal_state_yes = load_state('workbenches/wb_05_g.txt')        
    
    display_state(initial_state,'Initial state')
    
    display_state(goal_state_no,'\nUnreachable goal state')
    
    La_no = solve_1(initial_state,goal_state_no)
    print('\n\n')

    display_state(goal_state_yes,'\nReachable goal state')
    La_yes = solve_1(initial_state,goal_state_yes)
#    print(La_yes)
    
    test_passed =  (#1  
            La_no == 'no solution'
            and 
            (#2
                    La_yes ==  [(((5, 5, 5),), ((1, 1, 3, 1, 0), (0, 1, 0, 1, 1)), 1), 
                        (((1, 1, 3, 1, 0), (0, 1, 0, 1, 1), (0, 5, 5, 5, 0)), ((1, 2),), -2)]
                or
                    La_yes ==  [
                                ( ((1, 1, 3, 1, 0),(0, 1, 0, 1, 1)), ((1, 2),), -2) ,                            
                                ( ((5, 5, 5),),  ((0, 0, 1, 2, 0),(1, 1, 3, 1, 0),(0, 1, 0, 1, 1)), 1)
                                ]                
            )#2
        )#1
    
    return test_passed
    

# ---------------------------------------------------------------------------

def test_solve_2():
    '''
    Test function  'my_solver.solve_2'
    '''

    initial_state = load_state('workbenches/wb_05_i.txt')        
    goal_state_no = load_state('workbenches/wb_01_i.txt')        

    goal_state_yes = load_state('workbenches/wb_05_g.txt')        
    
    display_state(initial_state,'Initial state')
    
    display_state(goal_state_no,'Goal state "no"')
    
    La_no = solve_2(initial_state,goal_state_no)
    print('\n\n')

    display_state(goal_state_yes,'Goal state "yes"')
    La_yes = solve_2(initial_state,goal_state_yes)
#    print(La_yes)
    
    test_passed =  (#1  
            La_no == 'no solution'
            and 
            (#2
                    La_yes ==  [(((5, 5, 5),), ((1, 1, 3, 1, 0), (0, 1, 0, 1, 1)), 1), 
                        (((1, 1, 3, 1, 0), (0, 1, 0, 1, 1), (0, 5, 5, 5, 0)), ((1, 2),), -2)]
                or
                    La_yes ==  [
                                ( ((1, 1, 3, 1, 0),(0, 1, 0, 1, 1)), ((1, 2),), -2) ,                            
                                ( ((5, 5, 5),),  ((0, 0, 1, 2, 0),(1, 1, 3, 1, 0),(0, 1, 0, 1, 1)), 1)
                                ]                
            )#2
        )#1
    
    return test_passed

# ---------------------------------------------------------------------------

def test_solve_3a():
    '''
    Test function  'my_solver.solve_3'
    '''

    print('\n First test example \n')
    initial_state = load_state('workbenches/wb_06_i.txt')        
    goal_state = load_state('workbenches/wb_01_i.txt')        
    
    display_state(initial_state,'Initial state')

    goal_state = load_state('workbenches/wb_06_g.txt')        
    display_state(goal_state,'\nGoal state')
    La = solve_3(initial_state, goal_state)
    
    return La
#    ok_2 = La=='no solution'
#    
#    test_passed = ok_1 and ok_2
#    
#    return test_passed
# ---------------------------------------------------------------------------

def test_solve_3b():
    '''
    Test function  'my_solver.solve_3'
    '''

    print('\n First test example \n')
    initial_state = load_state('workbenches/wb_06_i.txt')        
    goal_state = load_state('workbenches/wb_06_g.txt')        
    
    display_state(initial_state,'Initial state')
    display_state(goal_state,'\nGoal state')
    
    La = solve_3(initial_state,goal_state)    
    
    print(La)


    return False #test_passed

# ---------------------------------------------------------------------------

def test_solve_4():
    '''
    Test function  'my_solver.solve_4'
    '''

    print('\n First test example \n')
    initial_state = load_state('workbenches/wb_06_i.txt')        
    goal_state = load_state('workbenches/wb_06_g.txt')        
    
    display_state(initial_state,'Initial state')
    display_state(goal_state,'\nGoal state')
    
    La = solve_4(initial_state,goal_state)    
    
    print(La)
    print('\n\n This problem is solvable \n')
    
    #


# ---------------------------------------------------------------------------

#    Below are some functions to help you debug your programs 

# ---------------------------------------------------------------------------
    
def gen_prob(ap, num_op, display=True):
    '''
    Given an assembly problem 'ap', generate a goal state by choosing 
    a sequence of random actions.
    
    Return the reachable goal state and a sequence of actions that lead
    to this goal state
    
    '''
    current_state = ap.initial
    display_state(current_state,"\nInitial state")
    
    for i in range(num_op):
        la = ap.actions(current_state)
        if len(la)==0:
            break
        ra = random.choice(la)
        current_state = ap.result(current_state, ra)
        if display:
            print('\n')
            display_state(current_state,"After action {} ".format(i+1))
    
    return current_state

# ---------------------------------------------------------------------------

def test_solve_rand_1():
    '''
    Generate a problem and attempt to solve it
    
    '''
    initial_state = load_state('workbenches/wb_09_i.txt')        
    ap_1 = AssemblyProblem_1(initial_state)
    
    # num_op=3 is fine
    goal_state = gen_prob(ap_1, num_op=4)
    
    t0 = time.time()

    La = solve_1(initial_state, goal_state)

    t1 = time.time()
    
    print ('Search solve_1 took {0} seconds'.format(t1-t0))

# ---------------------------------------------------------------------------

def test_solve_rand_2():
    '''
    Generate a problem
    
    '''
    initial_state = load_state('workbenches/wb_09_i.txt')        
    ap_2 = AssemblyProblem_2(initial_state)
    
    ap_1 = AssemblyProblem_1(initial_state)
    
    goal_state = gen_prob(ap_1, num_op=4)
    
    t0 = time.time()
    
    La = solve_2(initial_state, goal_state)
    print(La)

    
    t1 = time.time()
    
    print ('Search solve_1 took {0} seconds'.format(t1-t0))
    
# ---------------------------------------------------------------------------


def test_solve_1a():
    '''

    Run 'solve_1' on  
        initial_state : 'workbenches/wb_09_i.txt'
        goal_state : 'workbenches/wb_09_g1.txt'
    
    Computation takes about 20 minutes on my aging PC
    
    '''
    initial_state = load_state('workbenches/wb_09_i.txt')    

    goal_state  = load_state('workbenches/wb_09_g1.txt')
        
    t0 = time.time()
    
    La = solve_1(initial_state, goal_state)
    
    t1 = time.time()
    
    print ('Search solve_1 took {0} seconds'.format(t1-t0))
    
# ---------------------------------------------------------------------------

def test_solve_2a():
    '''

    Run 'solve_2' on  
        initial_state : 'workbenches/wb_09_i.txt'
        goal_state : 'workbenches/wb_09_g1.txt'
    
 
    Computation takes about a tenth of a second on my aging PC
   
    '''
    initial_state = load_state('workbenches/wb_09_i.txt')    

    goal_state  = load_state('workbenches/wb_09_g1.txt')
    
    
    t0 = time.time()
    
    La = solve_2(initial_state, goal_state)
    
    
    t1 = time.time()
    
    print ('Search solve_2 took {0} seconds'.format(t1-t0))
    

       
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    print(
'''
\n\n
This is *NOT* the script that will be used to mark your assignment.
Other examples will be used!
But, if your program does not pass the test functions provided in this file,
then it will not pass the test functions the markers will use.
\n\n
'''
        )

    #print('"test_appear_as_subpart" has been passed ', test_appear_as_subpart() )
    
    #print('\n"test_solve_1" has been passed ', test_solve_1() )

    print('\n"test_solve_2" has been passed ', test_solve_2() )

    #print('\ntest_solve_3a has been passed ', test_solve_3a() )

    #print('\ntest_solve_3b has been passed ', test_solve_3b() )

    
    #test_solve_4()

#    pass
    



    #test_solve_1a()
    
    #test_solve_rand_1()
    #test_solve_2a()
    
    #test_solve_rand_2()
    
