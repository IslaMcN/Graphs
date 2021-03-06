"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def add_undirected_edge(self, v1, v2):
        """
        Add an undirected edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise ValueError("vertex does not exist")

    
    
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError('Vertex does not exist')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #Create a queue 
        q = Queue()
        #Enqueue the starting vertex
        q.enqueue(starting_vertex)
        #Create a set to store visited vertices
        visited = set()
        #While the queue is not empty
        while q.size() > 0:
            #Dequeue the first vertex
            v = q.dequeue()
            #Check if it's been visited
            if v not in visited:
            #If it hasn't been visited
                print(v)
                visited.add(v)
                #Mark it as visited
                #Enqueue all it's neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            v= s.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.+

        What is my base case??
        If neighbor = None
        """
        # Create a stack
        stack = Stack()
        stack.push(starting_vertex)
        # Create a set to store visited vertices
        if visited is None:
            visited = set()
        
        # While the stack is not empty
        while stack.size() > 0:
            #Check to see if it's been visited
            v= stack.pop()
            
            #If it hasn't been visited
            if v not in visited:
                print(v)
                #Mark as visited
                visited.add(v)
                #Push all neighbors to stack
                for n in self.get_neighbors(v):
                    # if visited is None:
                    #     visited = set()
                   
                #Pass neighbors through again and again
                    self.dft_recursive(n, visited)
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.


        NOTE: I tried to use the Queue that was given to us and was unsuccessful
        It wasn't allowing me to subscript at all so I made my own that took in 
        regular python pop and append.

        """
        # Keep track of visited vertex
        visited = []
        # Keep track of the ones that need to be checked
        queue = [[starting_vertex]]
        # Return path if it has the start is the goal
        if starting_vertex == destination_vertex:
            return
        # Keep looping until all possible paths have been checked
        while queue:
            # Pop off the first path from the queue
            path = queue.pop(0)
            # Get the last node
            node = path[-1]
            if node not in visited:
                neighbors = self.get_neighbors(node)
                # Go through all neighbor nodes
                # Push it into the queue
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                    if neighbor == destination_vertex:
                        return new_path
                visited.append(node)
        return

    def dfs(self, starting_vertex, destination_vertex ):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = [(starting_vertex, [starting_vertex])]
        while stack:
            (vertex, path) = stack.pop()
            for n in self.vertices[vertex] - set(path):
                if n == destination_vertex:
                    return path + [n]
                else:
                    stack.append((n, path + [n]))
    
    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        path_copy = path.copy()
        path_copy.append(starting_vertex)
        if starting_vertex == destination_vertex:
            return path_copy
        if starting_vertex not in visited:
            for n in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(n, destination_vertex, visited, path_copy)
                if new_path is not None:
                    return new_path
        return None
            
               
            

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
