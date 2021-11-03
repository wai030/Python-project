import numpy as np
import time

state = np.zeros((3,3),dtype=np.int8)  #3 * 3 zero array, data type = integer

o=1
x=2


####################
## Drawing the board
####################

def show_board(state):
    print ("   0 1 2")
    print ("   ======")
    
    for r in range(0,3):        
        print (r, str(state[r]).replace("0", " ").replace("1", "O").replace("2", "X"))
        
####################
## Win Function
####################
        
def win(state):
    if np.equal(state.diagonal(), [1,1,1]).all() or np.equal(np.flip(state,1).diagonal(), [1,1,1]).all() :
        
        return 1
    if np.equal(state.diagonal(), [2,2,2]).all() or np.equal(np.flip(state,1).diagonal(), [2,2,2]).all():
        
        return 2
    for i in range(3):
        if np.equal(state[i,:],[1,1,1]).all():
            
            return 1
        if np.equal(state[i,:],[2,2,2]).all():
            
            return 2
        if np.equal(state[:,i],[1,1,1]).all():
            
            return 1
        if np.equal(state[:,i],[2,2,2]).all():
            
            return 2
            

    return 0
    #
    #   Write your code here
    #   Return 1 if 1 wins in state 
    #   Return 2 if 2 wins in state
    #   Return 0 otherwise
    #
    #   You need to check:
    #      each column
    #      each row 
    #      the two diagonals
    #
    

    
#################
## Main
##################
state = np.array ([[0, 1, 1],[2, 2, 0],[0, 0, 0]])
print (state)
winner = win(state)
print ("1 Winner: ", winner)
assert(winner==0), "XXXXX Case 1 failed"


state = np.array ([[0, 1, 1],
               [2, 2, 2],
               [0, 0, 1]])
print (state)
winner = win(state)
print ("2 Winner: ", winner)
assert(winner==2), "XXXXX Case 2 failed"


state = np.array ([[2, 1, 1],
               [2, 2, 1],
               [1, 2, 1]])
print (state)
winner = win(state)
print ("3 Winner: ", winner)
assert(winner==1), "XXXXX Case 3 failed" 

state = np.array ([[2, 1, 1],
               [0 ,2, 1],
               [0, 0, 2]])

print (state)
winner = win(state)
print ("4 Winner: ", winner)
assert(winner==2),"XXXXX Case 4 failed"


state = np.array ([[2, 1, 1],
               [1 ,1, 2],
               [1, 2, 2]])

print (state)
winner = win(state)
print ("5 Winner: ", winner)
assert(winner==1),"XXXXX Case 5 failed" 


state = np.array ([[2, 1, 1],
               [1 ,2, 2],
               [1, 2, 1]])

print (state)
winner = win(state)
print ("6 Winner: ", winner)
assert(winner==0),"XXXXX Case 6 failed"


input()
