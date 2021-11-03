###################
## Variable Domains
###################

domain = (1,2,3,4)

######################################################
## Definition of a state (i.e., what the variables are
######################################################

start_state = [ None,1   ,None,3   ,
                4   ,None,None,2   ,
                None,2   ,None,None,
                3   ,None,2   ,1   ]


def display_solution (state):
    
    print ("[{},{},{},{},".format(state[0],state[1],state[2],state[3]))
    print (" {},{},{},{},".format(state[4],state[5],state[6],state[7]))
    print (" {},{},{},{},".format(state[8],state[9],state[10],state[11]))
    print (" {},{},{},{}]".format(state[12],state[13],state[14],state[15]))

##########################################
## Functions related to the problem domain
##########################################

def is_goal(state):
    
    if 0 in state:
        return False
        
    if not satisfy_constraints(state):
        return False
    
    return True

##########################################
## Constraints
##########################################
		 
#   If either is None (unassigned), or the two are not the same
def check_constraint_1 (x, y):    
    if x!=y:
        return True
    else:
        return False
               

def satisfy_constraints(state):
    for i in range(16):
        j=i%4
        h=i//4
        if state[i]!= 0:
            for z in range(4):
                
                if (4*h+z == i):
                    z+=1
                    
                elif (state[i] == state[4*h+z]):
                    
                    return False
            for g in range(4):
                if (4*g+j == i):
                    g+=1
                elif ( state[i] == state[4*g+j]):
                
                    return False
    return True

##################
## Search Function
##################
def find_children(state):
    
    if 0 in state:
        children=[]
        
        none_idx = state.index(0)
        
        for value in domain:
            child = state.copy()
            child[none_idx] = value
            children.append(child)        
        return children
    else:
        
        return 0
    

def csp_search(start_state):
    
    to_visit = []
    next_state = start_state

    end = False
    
    while not end: 
        
        if is_goal(next_state):
            display_solution (next_state)
            print("Solution Found!")                                    
            end = True

        else:

            for child_state in find_children(next_state):
                if satisfy_constraints(child_state):
                     
                     to_visit.append(child_state)
			
            if to_visit:
                next_state=to_visit.pop()
            else:
                print("Failed to find a goal state")
                end=True


##################
## Main
##################
x=[]
for i in range(1, 5):
    a = input("Enter {}  row (enter 0 for space): ".format(i))
    x += a.split( )
x= list(map(int, x))
csp_search(x)

input()
