############################
## Tree/Graph data structure
#############################

graph = {1: [2, 3], 
         2: [4, 5], 3: [6, 7]}

goal = 5

##########################################
## Functions related to the problem domain
##########################################

def is_goal(x):
    return x==goal
		 

##################
## Search Function
##################
def find_children(node):
    children = graph.get(node)
    if children:
        return children
    else:
        return []

def dfs_search(start_node):
    next_node = start_node 
    visited = []
    to_visit = []

    end = False
    while not end: 
        if not next_node in visited:
            print("Visiting node {} ".format(next_node))
            visited.append(next_node)
            if is_goal(next_node):
                print("Goal reached")
                end = True
            else:
                for child_node in find_children(next_node):
                    to_visit.append(child_node)
			
        if to_visit:
            next_node=to_visit.pop(0)        
        elif not end:
            print("Failed to find a goal state")
            end=True


##################
## Main
##################
  
dfs_search(1)

input()
