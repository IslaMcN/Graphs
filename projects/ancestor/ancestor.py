# Describe:
    # What are the nodes?
        #Parent and Children
    # What algo should I use?
        # BFS

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
        return vertex_id

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
    
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        print('neighbors', vertex_id)
        # else:
        #     raise ValueError('Vertex does not exist')
        return None

            
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    queue = Queue()
    queue.enqueue([starting_node])
    visited = set()
    ancestor = -1
    path = []
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        if parent not in graph.vertices:
            graph.add_vertex(parent)
        if child not in graph.vertices:
            graph.add_vertex(child)
        graph.add_edge(child, parent)
    ## Check length of path and pick and return the longest
    # Update ancestors
    longest_path = 1
    while queue.size() > 0:
        path = queue.dequeue()
        v = path[-1]
        if len(path) == longest_path:
            if v < ancestor:
                longest_path = len(path)
                ancestor = v
        if len(path) > longest_path:
            longest_path = len(path)
            ancestor = v
        
        print(len(graph.get_neighbors(v)))
        if len(graph.get_neighbors(v)) != 0:
            print('here', v)
            ancestor = v
        if v not in visited:
            visited.add(v)
            for n in graph.get_neighbors(v):
                path_copy = path.copy()
                path_copy.append(n)
                queue.enqueue(path_copy)
    print(ancestor)
    return ancestor
            











