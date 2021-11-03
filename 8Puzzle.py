#
#  STUDENT ID:
#  STUDENT NAME:
#
#
import time

#
### Representation
# The squares are represented as Lists.
#
# E.g. [0,3,6,1,4,7,2,5,8] represents the following state:
#
# -------------
# | 0 | 3 | 6 |
# -------------
# | 1 | 4 | 7 |
# -------------
# | 2 | 5 | 8 |
# -------------
#
# The goal is defined as:
#    Values                Index 
# -------------      # -------------      
# | 1 | 2 | 3 |	     # | 0 | 1 | 2 |
# -------------      # -------------
# | 4 | 5 | 6 |      # | 3 | 4 | 5 | 
# -------------      # -------------
# | 7 | 8 | 0 |      # | 5 | 6 | 8 |
# -------------      # ------------- 
#
# Where 0 denotes the blank tile or space.
#         idx  0  1  2  3  4  5  6  7  8
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

EMPTY_TILE = 0

def display( state ):
        print ("-------------")
        print ("| {} | {} | {} |".format(state[0], state[1], state[2]).replace('0', ' '))
        print ("-------------")
        print ("| {} | {} | {} |".format(state[3], state[4], state[5]).replace('0', ' '))
        print ("-------------")
        print ("| {} | {} | {} |".format(state[6], state[7], state[8]).replace('0', ' '))
        print ("-------------")
	
def swap(state, pos_1, pos_2):
	temp = state[pos_1]
	state[pos_1] = state[pos_2]
	state[pos_2] = temp

def is_goal(state):
        return state == goal_state
	
def move_up( state ):
	"""Moves the blank tile up on the board. Returns a new state as a list."""
	# Perform an object copy
	new_state = state.copy() 
	empty_position = new_state.index(EMPTY_TILE)
	 
	swap(new_state, empty_position, empty_position-3)		
	return new_state
	

def move_down( state ):
	"""Moves the blank tile downon the board. Returns a new state as a list."""
	# Perform an object copy
	new_state = state.copy() 
	empty_position = new_state.index(EMPTY_TILE)
	 
	swap(new_state, empty_position, empty_position+3)		
	return new_state
	

def move_left( state ):
	"""Moves the blank tile leftward. Returns a new state as a list."""
	# Perform an object copy
	new_state = state.copy() 
	empty_position = new_state.index(EMPTY_TILE)
	 
	swap(new_state, empty_position, empty_position-1)		
	return new_state

def move_right( state ):
	"""Moves the blank tile rightward. Returns a new state as a list."""
	# Perform an object copy
	new_state = state.copy() 
	empty_position = new_state.index(EMPTY_TILE)
	 
	swap(new_state, empty_position, empty_position+1)		
	return new_state
	

		
def create_path(path, state):
        new_path=path.copy()
        new_path.append(state)
        return(new_path)
        
def find_children(state):
        children=[]
        if state.index(EMPTY_TILE) not in (0,1,2):
                children.append(move_up(state))
        if state.index(EMPTY_TILE) not in (6,7,8):
                children.append(move_down(state))
        if state.index(EMPTY_TILE) not in (0,3,6):
                children.append(move_left(state))
        if state.index(EMPTY_TILE) not in (2,5,8):
                children.append(move_right(state))
        return children        


#
#  h1 heuristic: number of wrong tiles
#
#Estimate how far away is the solution by counting the number of tiles in wrong position.
#RETURN: an integer for the number of wrong tiles
def h1(state):
	################################
	#   WRITE YOUR CODE HERE
	################################
    i=0
    j=0
    while i in range(0,8):
        if(state[i] != goal_state[i]):
            j+=1
        i+=1
        return j
	 
#
#  h2 heuristic: Manhattan Distance
#Estimate how far away is the solution according to the total Manhattan distance
#RETURN: an integer for the total Manhattan distance between each tile and its correct position 
       
def h2(state):
    i=0
    n=0
    for i in range(0, 8):
        
        if(state[i] != goal_state[i]):
            a=state[i]-1
            b=a-i
            
            if (b%3==0):
                        n= n + b/3
            elif (b%3 ==1 or b%3 ==-1):
                n= n + b//3 + 1
                
            elif (b%3 ==2 or b%3 == -1):
                n= n + b//3 + 2
            i+=1    
    return n
	##############################
	#   WRITE YOUR CODE HERE
	##############################
	
                
        
def find_lowest_f(to_visit):


        """  Loop through all items in the to_visit list, and return the node n with the lowest f(n) score
               where f(n) = g(n)+ h(n)

               Make sure you also remove the selected notes from the to_visit list before returning it.

               Note: the structure of the to_visit list is:
                    [ [state_1, g(state_1), h(state_1), [path_1]],
                      [state_2, g(state_2), h(state_2), [path_2]],
                      [state_3, g(state_3), h(state_3), [path_3]],
                       ...
                    ]                    

                return: the node for the state to be visted next, which is also a list of [state, g_score, h_score, path]
        """

	
        lowest_f =  99999999
        
        chosen_note =[]
        for node in to_visit:
                (state, g, h, path) = node
                f = g + h             
                if f < lowest_f:                        
                        lowest_f =f
                        chosen_node=node                        
                        
        to_visit.remove(chosen_node)
        return chosen_node
                        
                


# Main method

nodes_visited_count = 0

def a_star(start_state, heuristic):
	
        path = [start_state]  
        next_node = (start_state, 0 , heuristic(start_state), path)  #node=[state, g(state), h(state), path]
        visited = []
        to_visit = []
	
        end = False
               
        while not end:
                
                (next_state, g, h, path) = next_node
                
                #print(next_state, g,h)
                if not next_state in visited:
                        visited.append(next_state)        
                        if is_goal(next_state):
                                print("Goal reached!")
                                end = True
                                return path
                        else:
                                for child_state in find_children(next_state):
                                        child_path = create_path(path, child_state)                    
                                        to_visit.append([child_state, g+1, heuristic(child_state), child_path])
                               
                if to_visit:
                        next_node=find_lowest_f(to_visit)
                else:
                        print("Failed to find a goal state")
                        end=True
        return []

def main():			
        
        #start_state =[1,0,3,4,2,5,6,7,8]   #easy
        #start_state =[5,1,3,4,0,8,7,6,2]   #easy 
        start_state =[6,4,3,1,0,8,5,2,7]   #medium         
        #start_state =[4,7,2,8,0,1,3,6,5]   #hard
        #start_state =[1,7,4,2,3,8,0,6,5]    #hard
        

        time1 = time.time()

        #path = a_star(start_state, h1)   #h1() ; number of wrong tiles heuristic
        path = a_star(start_state, h2)   #h2() ; Manhanttan distance heuristic 

        if path:       
                for state in path:
                        display(state)
                        print()
                        
        time2 = time.time()
        print ("Time", time2-time1)       
        
          		

# If the file is being run executed directly, call the main() function.
if __name__ == "__main__":
        main()
        input()
