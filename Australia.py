###################
## Variable Domains
###################

domain = ("R", "G", "B")

######################################################
## Definition of a state (i.e., what the variables are
######################################################
  
#               WA   NT   SA   Q   NSW  V
start_state = [None,None,None,None,None,None]


def display_solution (state):
    (WA, NT, SA, Q, NSW,  V) = state
    print ("WA={} NT={} SA={} Q={} NSW={} V={}".format(WA, NT, SA, Q, NSW,  V))

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
		 
#   If either is None (unassigned), or the two are not the same
def check_constraint_1 (x, y):    
    if x!=y:
        return True
    else:
        return False
               

def satisfy_constraints(state):
    (WA, NT, SA, Q, NSW, V) = state
    
    to_check=[(WA, NT), (WA, SA), (NT, SA), (NT, Q), (Q, SA), (Q, NSW),(NSW, V), (NSW, SA)]    
    
    for s1, s2 in to_check:    
        if s1 != None and s2!= None: 
            if s1==s2: # constraint not satified            
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
            print("Failed to find a goal state")
            end=True


##################
## Main
##################

csp_search(start_state)

input()
