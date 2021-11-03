import numpy as np
import time

state = np.zeros((3,3),dtype=np.int8)  #3 * 3 zero array, data type = integer


o=1  #player 1 uses o
x=2  #player 2 uses x


####################
## Drawing the board
####################

def show_board():
    print ("   0 1 2")
    print ("   ======")
    
    for r in range(0,3):        
        print (r, str(state[r]).replace("0", " ").replace("1", "O").replace("2", "X"))
        
####################
## Scoring Functions
####################

def score1(array):
    score=0
    sorted = np.sort(array)
    
    if np.equal(sorted, [0,o,o]).all():     
        return 1
    if np.equal(sorted, [0,x,x]).all():        
        return -1
    return 0

def score(state):

    if win(state) == o:
        return 999
    if win(state) == x:
        return -999
    
    score=0

    for c in state.T:   #score for each column
        score+= score1(c)
    for r in state:     #score for each row
        score+= score1(r)
        
    score+= score1(state.diagonal())   #score for diagonal  /
    score+= score1(np.flip(state,1).diagonal()) #score for the oppsite diagonal \

    return score
    
        

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
	

####################
## Search Functions 
####################
        
def list_moves(state):
    children=[]
    for i in range(0,3):
        for j in range(0,3):
            if state[i,j]==0:
                children.append([i,j])
    return children    


def max_value(state, level):
    """ Return the computed score of the state, and the coordinate of the best next move (if any)
        Assuming the current player is player1 (Max player)    
            argument: state: the state to be evaluated
            level: the number of the level to be searched
    """

    if level ==0 or np.count_nonzero(state)==9:
        return score(state), None, None
    
    if win(state) ==o:
        return 999, None, None

    if win(state) ==x:
        return -999, None, None

    max_score=-9999
    best_i=-1; best_j=-1
    for move in list_moves(state):
        i,j = move
        child_state = np.copy(state)
        child_state[i,j] = o
 
        value,dummy1, dummy2 = min_value(child_state, level-1)  
        if value > max_score:
                max_score=value
                best_i, best_j = i,j
    return (max_score, best_i, best_j)
            
            
def min_value(state, level):
    """ Return the computed score of the state, and the coordinate of the best next move (if any)
        Assuming the current player is player2 (Min player)    
            argument: state: the state to be evaluated
            level: the number of the level to be searched
    """
    if level ==0 or np.count_nonzero(state)==9:
        return score(state), None, None
    if win(state) ==o:
        return 999, None, None
    if win(state) ==x:
        return -999, None, None

    min_score=9999
    best_i=-1; best_j=-1
    for i,j in list_moves(state):       
        child_state = np.copy(state)
        child_state[i,j] = x
        value,dummy1, dummy2 = max_value(child_state, level-1)
        if value < min_score:
                min_score=value
                best_i, best_j = i,j
    return (min_score, best_i, best_j)
    
        
############# 
## Game Play 
#############

def computer_move(turn):

    print("Computing is thinking...")
    if (turn == o):
        value, x, y = max_value(state, MAX_PLY)
    else:
        value, x, y = min_value(state, MAX_PLY)

    state[x,y]=turn
    
            
def player_move(turn):
    
    ok=False
    while not ok:
        try:
            x,y = [int(x) for x in input("Enter the ROW and COL of your move: ").split()]
            if state[x,y]==0:
                ok=True
                state[x,y]=turn
            else:
                print("Invalid move")
        except:
            print("Invalid move")
            
    
def play_game():
    turn =o
    end=False
    show_board()
    move_count =1

    global xDEBUG
    while not end:
        
        if turn ==o:
            player_move(o)
            #computer_move(o)
        else:            
            #player_move(x)
            computer_move(x)
            
        show_board()
        print ("score = {} ".format(score(state)))

        if win(state)==turn:            
            print("Player {} win!".format(turn))
            end=True

        if move_count ==9:
            end=True
            print("Draw!")
        else:
            move_count = move_count+1

            
        if turn ==o:
            turn =x
        else:
            turn = o
        
                
    
#################
## Main
##################


MAX_PLY =1
time1 = time.time()
play_game()
time2 = time.time()

print ("Time", time2-time1)
input()
