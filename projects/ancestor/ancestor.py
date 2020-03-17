# Using Depth-First Search
    # This is usually a good approach if you want the solution that is very far from the root.
def earliest_ancestor(ancestors, starting_node):
    #Begin at starting vertex
    stack = [starting_node]
    #Explore the vertex
    explored = set()
        #If unexplored, adjacent vertex
    if starting_node not in explored:
            #Explore adjacent vertex
        adjacent = next(stack)
        # Mark explored once all adjacent vertices have been explored (remove from 
        # stack)
    x = stack.pop()
    explored.add(x)
    