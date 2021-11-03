
###################
## Variable Domains
###################

domain = range(8)

######################################################
## Definition of a state (i.e., what the variables are
######################################################
  
#              row1,row2,row3,row4,row5,row6,row7,row8
start_state = [None,None,None,None,None,None,None,None]


def display_solution (state):
        
    print(state)
    for i in range(8):
        col=state[i]                
        print("I", end = "")
        for j in range(col):
            print(".", end="")           
        print("O", end="")
        for j in range(col+1,8):
            print(".", end="")           
        print("]") 

##########################################
## Functions related to the problem domain
##########################################

def is_goal(state):
    
    if None in state:
        return False
        
    if not satisfy_constraints(state):
        return False
    
    return True

##########################################
## Constraints
##########################################
		 


def satisfy_constraints(state):
        
    for r1 in range(8):
        for r2 in range(r1+1,8):        
            c1=state[r1]
            c2=state[r2]
            if c1 != None and c2!= None: 
                if c1==c2:
                    return False
                if abs(c1-c2) == abs(r1-r2):              
                    return False
    
    return True

##################
## Search Function
##################
def find_children(state):
       
    if None in state:
        children=[]
        none_idx = state.index(None)
        for value in domain:
            child = state.copy()
            child[none_idx] = value
            children.append(child)        
        return children
    else:
        return None
    

def csp_search(start_state):
     
    to_visit = []
    next_state = start_state

    end = False
    
    while not end: 
        
        if is_goal(next_state):
            print("Solution Found!")
            display_solution(next_state)
            end = True

        else:

            for child_state in find_children(next_state):                
                if satisfy_constraints(child_state):
                     to_visit.append(child_state)
			
        if to_visit:
            next_state=to_visit.pop()
        else:
            if not end:
                print("Failed to find a goal state")
                end=True


##################
## Main
##################

csp_search(start_state)
#print(satisfy_constraints([4,0,7,3,1,6,2,5]))

input()
