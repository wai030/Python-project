import copy 
#Missionaries and Cannibals (Missionaries and Cannibals)


#######################
## Data Structures ####
#######################
#  The following is how the state is represented during a search.
#  A dictionary format is chosen for the convenience and quick access 

LEFT=0; RIGHT=1; BOAT_POSITION=2
Missionaries=0;Cannibal=1

#[[num_Missionaries_left, num_Cannibal_left], [num_Missionaries_right, num_Cannibal_right], boat_position (0=left, 1=right)]
initial_state = [[0,0],[3,3], RIGHT]
goal_state = [[3,3],[0,0], LEFT]


###################################################
## Functions related to the game
###################################################


# Verifies if the state is safe.

def is_safe(state):
     
      
    return (not (0 < state[LEFT][Missionaries] < state[LEFT][Cannibal] or
                 0 < state[RIGHT][Missionaries] < state[RIGHT][Cannibal] )
            )
        

def opposite_side(side):
    if side == LEFT:
        return RIGHT
    else:
        return LEFT
    
##############################################
## Functions for recording the path #########
##############################################

#
# A path is the states from the root to a certain goal node
# It is represented as a List of states from the root
# The create_path function create a new path by add one more node to an old path
#

def create_path(old_path, state):    
    new_path = old_path.copy()
    new_path.append(state)
    return new_path

##########################
## Functions for Searching
##########################

def move(state, Missionariess, Cannibals):
    side = state[BOAT_POSITION]
    opposite = opposite_side(side)
    
    if state[side][Missionaries] >= Missionariess and state[side][Cannibal] >=Cannibals:
        new_state= copy.deepcopy(state)
        new_state[side][Missionaries]-=  Missionariess
        new_state[opposite][Missionaries] +=  Missionariess
        new_state[side][Cannibal] -=  Cannibals
        new_state[opposite][Cannibal] +=  Cannibals
        new_state[BOAT_POSITION]   =   opposite

    return new_state
        
    

# Find out the possible moves, and return them as a list
def find_children(old_state):
    children = []
    side = old_state[BOAT_POSITION]

    # Try to move one Missionary
    if old_state[side][Missionaries] > 0:
        new_state= move(old_state, Missionariess=1, Cannibals=0)
    
        if is_safe(new_state):
            children.append(new_state)          
                  
    # Try to move one Cannibal
    if old_state[side][Cannibal] > 0:
        new_state= move(old_state, Missionariess=0, Cannibals=1)
    
        if is_safe(new_state):
            children.append(new_state)          
    
    # Try to move one Missionaries and one Cannibal
    if old_state[side][Cannibal] > 0 and old_state[side][Missionaries] > 0:
    
        new_state= move(old_state, Missionariess=1, Cannibals=1)
            
        if is_safe(new_state):
            children.append(new_state)
        

    # Try to move two Missionariess
    if old_state[side][Missionaries] > 1:
        new_state= move(old_state, Missionariess=2, Cannibals=0)
        if is_safe(new_state):
            children.append(new_state)          
    # Try to move two Cannibals
    if old_state[side][Cannibal] > 1:
        new_state= move(old_state, Missionariess=0, Cannibals=2) 
        if is_safe(new_state):
            children.append(new_state)          

    return children

#  ---------------------------
# Search routine ####
#  ---------------------------
def bfs_search(start_state):

         
    visited = []
    to_visit = []

    path = create_path([], start_state)        
    next_node =[start_state, path]

                
    end = False
    while not end:

        next_state, path = next_node

        
        if not next_state in visited:
            
            visited.append(next_state)
            if next_state == goal_state:
        
                return path 
            else:
                for child_state in find_children(next_state):
                    child_path = create_path(path, child_state)
                    to_visit.append([child_state, child_path])

        
                			
        if to_visit:
            next_node=to_visit.pop(0)
        else:
            print("Failed to find a goal state")
            end=True
            return ()   
        


################
## Main   ######
################

# Search for a solution 
path = bfs_search(initial_state)

if path: 
    print ("Path from start to goal:")
    for p in path:
        left,right,side = p
        t_left, b_left=left
        t_right, b_right=right

        if side==LEFT:
            boat_l = "#BOAT#";boat_r = "      "
        else:    
            boat_l = "      ";boat_r = "#BOAT#"
        print(" Missionaries {}  Cannibal {} {} |~~~~~| {}  Missionaries {}  Cannibal {}" .format(t_left, b_left, boat_l, boat_r, t_right, b_right))

input()
