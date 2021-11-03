###################
## Variable Domains
###################

domain = (1,2,3,4,5,6,7,8,9)

######################################################
## Definition of a state (i.e., what the variables are
######################################################



def display_solution (state):
    
    print ("[{},{},{},{},{},{},{},{},{}".format(state[0],state[1],state[2],state[3],state[4],state[5],state[6],state[7],state[8]))
    print (" {},{},{},{},{},{},{},{},{}".format(state[9],state[10],state[11],state[12],state[13],state[14],state[15],state[16],state[17]))
    print (" {},{},{},{},{},{},{},{},{}".format(state[18],state[19],state[20],state[21],state[22],state[23],state[24],state[25],state[26]))
    print (" {},{},{},{},{},{},{},{},{}".format(state[27],state[28],state[29],state[30],state[31],state[32],state[33],state[34],state[35]))
    print (" {},{},{},{},{},{},{},{},{}".format(state[36],state[37],state[38],state[39],state[40],state[41],state[42],state[43],state[44]))
    print (" {},{},{},{},{},{},{},{},{}".format(state[45],state[46],state[47],state[48],state[49],state[50],state[51],state[52],state[53]))
    print (" {},{},{},{},{},{},{},{},{}".format(state[54],state[55],state[56],state[57],state[58],state[59],state[60],state[61],state[62]))
    print (" {},{},{},{},{},{},{},{},{}".format(state[63],state[64],state[65],state[66],state[67],state[68],state[69],state[70],state[71]))
    print (" {},{},{},{},{},{},{},{},{}]".format(state[72],state[73],state[74],state[75],state[76],state[77],state[78],state[79],state[80]))

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
    for i in range(81):
        j=i%9
        h=i//9
        if state[i]!= 0:
            for z in range(9):
                
                if (9*h+z == i):
                    z+=1
                    
                elif (state[i] == state[9*h+z]):
                    
                    return False
            for g in range(9):
                if (9*g+j == i):
                    g+=1
                elif ( state[i] == state[9*g+j]):
                
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
for i in range(1,10):
    a = input("Enter {}  row (enter 0 for space): ".format(i))
    x += a.split( )
    i+=1
x= list(map(int, x))
csp_search(x)

input()
