import copy 
#Missionaries and Cannibals (Missionaries and Cannibals)


#######################
## Data Structures ####
#######################
#  The following is how the state is represented during a search.
#  A dictionary format is chosen for the convenience and quick access 

LEFT=0; RIGHT=1; BOAT_POSITION=2
goat=0; wolf=1; cabbage=2

#[[num_Missionaries_left, num_Cannibal_left], [num_Missionaries_right, num_Cannibal_right], boat_position (0=left, 1=right)]
initial_state = [{"goat": 0, 'wolf':0, 'cabbage':0},{'goat':1, 'wolf':1, 'cabbage':1}, RIGHT]
goal_state = [{'goat':1, 'wolf':1, 'cabbage':1},{'goat':0, 'wolf':0, 'cabbage':0}, LEFT]


###################################################
## Functions related to the game
###################################################


# Verifies if the state is safe.

def is_safe(state):
    
      
    return (
          not((state[LEFT].get('goat')==1 and state[LEFT].get('wolf')==1 and state[LEFT].get('cabbage')==0 and state[BOAT_POSITION]==1) or
             (state[RIGHT].get('goat')==1 and state[RIGHT].get('wolf')==1 and state[RIGHT].get('cabbage')==0 and state[BOAT_POSITION]==0) or
             (state[LEFT].get('goat')==1 and state[LEFT].get('wolf')==0 and state[LEFT].get('cabbage')==1 and state[BOAT_POSITION]==1) or
             (state[RIGHT].get('goat')==1 and state[RIGHT].get('wolf')==0 and state[RIGHT].get('cabbage')==1 and state[BOAT_POSITION]==0))
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

def move(state, wolfs, goats, cabbages):
    
    side = state[BOAT_POSITION]
    
    opposite = opposite_side(side)
    
    if state[side].get('goat') >= goats and state[side].get('wolf') >=wolfs and state[side].get('cabbage') >= cabbages:
        new_state= copy.deepcopy(state)
        new_state[side]['goat'] -= goats
        new_state[opposite]['goat'] +=  goats
        new_state[side]['wolf'] -=  wolfs
        new_state[opposite]['wolf'] +=  wolfs
        new_state[side]['cabbage']-=  cabbages
        new_state[opposite]['cabbage'] +=  cabbages
        new_state[BOAT_POSITION]   =   opposite
        
    return new_state
        
    

# Find out the possible moves, and return them as a list
def find_children(old_state):
    children = []
    side = old_state[BOAT_POSITION]

    
        
    
    
    # Try to move one wolf
    if old_state[side].get('wolf') > 0:
        
        new_state= move(old_state, 1, 0, 0)
        
        if is_safe(new_state):
            
            children.append(new_state)          
            
    # Try to move one goat
    if old_state[side].get('goat') > 0:
        
        new_state= move(old_state, 0, 1, 0)
    
        if is_safe(new_state):
           
            children.append(new_state)          
            
    # Try to move one cabbage
    if old_state[side].get('cabbage') > 0 :
            
        new_state= move(old_state, 0, 0, 1)
            
        if is_safe(new_state):
            
            children.append(new_state)
                
    if old_state[side]:
        new_state= move(old_state, 0, 0, 0)
            
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
    this = False
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
            if this!=True:
                this= True
               
            else:
           
                end=True
                print("Failed to find a goal state")
                
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
        
        
        g_left, w_left, c_left=left
        g_right, w_right, c_right=right

        if side==LEFT:
            boat_l = "#BOAT#";boat_r = "      "
        else:    
            boat_l = "      ";boat_r = "#BOAT#"
        print("wolfs {}  goats {}  cabbages {}  {} |~~~~~| {}  wolfs {}  goats {}  cabbages {}" .format(left[w_left], left[g_left], left[c_left], boat_l, boat_r, right[w_right], right[g_right], right[c_right]))

input()
