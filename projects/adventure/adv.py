from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()
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

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
current = world.starting_room
traversal_path = None
# CREATE EMPTY STACK
stack = Stack()
# ADD STARTING ROOM TO STACK
stack.push(current)
print('Start:', stack)
# CREATE AN EMPTY SET TO STORE VISITED NODES
visited = set()
# WHILE THE STACK IS NOT EMPTY
while stack.size > 0:
    # POP THE FIRST ROOM
    v = stack.pop()
    # CHECK IF IT HAS BEEN VISITED
    # IF IT HAS NOT BEEN VISITED
    if v not in visited:
        # MARK IT AS VISITED
        print(v)
        visited.add(v)
         
        # CHECK IF ITS NEIGHBORS HAVE BEEN VISITED
        if v.w_to and v.w_to not in visited:
            traversal_path.append('w')
            stack.push(v.w_to)
        elif v.n_to and v.n_to not in visited:
            traversal_path.append('n')
            stack.push(v.n_to)
        elif len(visited) == len(room_graph):
            print(visited)
            break
        elif v.s_to and v.s_to not in visited:
            traversal_path.append('s')
            stack.push(v.s_to)
        elif v.e_to and v.e_to not in visited:
            traversal_path.append('e')
            stack.push(v.e_to)
        # IF NOT, GO TO ONE OF THE DIRECTIONS
        # IF ALL NEIGHBORS HAVE BEEN VISITED, USE BFS TO FIND THE FIRST ROOM THAT HAS 
        # EXPLORED NEIGHBOR
        # DFS
        # CREATE EMPTY QUEUE
        queue = Queue()
        # ADD THE ROOM THAT HAS THE NON-EXPLORED NEIGHBOR TO THE QUEUE AS THE STARTING 
        # POINT OF THE PATH
        paths = [[]]
        # WHILE THE STACK IS NOT EMPTY
        while queue.size > 0:
            # POP THE FIRST ROOM
            visited_room = queue.dequeue()
            path = paths.pop(0)
            # CHECK THIS VISITED ROOM TO SEE IF IT HAS UNEXPLORED NEIGHBOR
            if (visited_room.n_to and visited_room.n_to not in visited) or (visited_room.s_to and visited.s_to not in visited) or (visited_room.w_to and visited_room.w_to not in visited) or (visited_room.e_to and visited_room.e_to not in visited):
                queue.queue.clear()
                traversal_path.extend(path)
                stack.push(visited_room)

        


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
