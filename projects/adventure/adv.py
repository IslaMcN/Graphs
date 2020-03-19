from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "projects/adventure/maps/test_line.txt"
# map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.directions = {0:
        {
            'n': '?', 's': '?', 'e': '?', 'w': '?'
        }}
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        print(vertex_id)
        print(self.vertices)
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            self.add_vertex(vertex_id)
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
#initialize
    def maze(self, starting):
        stack = Stack()
        traversal_path = []
        stack.push(starting)
        # Create Graph
        if starting not in self.vertices:
            self.add_vertex(starting)
#Use DFT - Recursion
        while stack.size() > 0:
            node = stack.pop()
            if node not in traversal_path:
                print(node)
                traversal_path.append(node)
                for n in self.get_neighbors(node):
                    stack.push(n)
# TRAVERSAL TEST
        visited_rooms = set()
        player.current_room = world.starting_room
        visited_rooms.add(player.current_room)

        for move in traversal_path:
            player.travel(move)
            visited_rooms.add(player.current_room)

        if len(visited_rooms) == len(room_graph):
            print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
        else:
            print("TESTS FAILED: INCOMPLETE TRAVERSAL")
            print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

Graph().maze(000)

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
