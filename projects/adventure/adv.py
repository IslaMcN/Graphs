from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
#DFS
stack=[]
stack.append(world.starting_room)
print("start", stack)
visited = set()
while len(stack) > 0:
    room = stack.pop()
    if room not in visited:
        print("stack",room.name)
        visited.add(room)
    if room.w_to and room.w_to not in visited:
        traversal_path.append("w")
        stack.append(room.w_to)
    elif room.s_to and room.s_to not in visited:
        traversal_path.append("s")
        stack.append(room.s_to)
    elif room.n_to and room.n_to not in visited:
        traversal_path.append("n")
        stack.append(room.n_to)
    elif room.e_to and room.e_to not in visited:
        traversal_path.append("e")
        stack.append(room.e_to)
    
    elif len(visited) == len(room_graph):
        print(visited)
        break

    else:
        # Bfs
        queue = []
        queue.append(room)
        paths = [[]]
        while len(queue) > 0:
            visited_room = queue.pop(0)
            path = paths.pop(0)
            if (visited_room.n_to and visited_room.n_to not in visited) or (visited_room.s_to and visited_room.s_to not in visited) or (visited_room.w_to and visited_room.w_to not in visited) or (visited_room.e_to and visited_room.e_to not in visited):
                print("queue", visited_room.name)
                queue.clear()
                traversal_path.extend(path)
                stack.append(visited_room)
            else:
                
                if visited_room.n_to:
                    new_path = path.copy()
                    new_path.append("n")
                    paths.append(new_path)
                    queue.append(visited_room.n_to)
                if visited_room.s_to:
                    new_path = path.copy()
                    new_path.append("s")
                    paths.append(new_path)
                    queue.append(visited_room.s_to)
                if visited_room.w_to:
                    new_path = path.copy()
                    new_path.append("w")
                    paths.append(new_path)
                    queue.append(visited_room.w_to)
                if visited_room.e_to:
                    new_path = path.copy()
                    new_path.append("e")
                    paths.append(new_path)
                    queue.append(visited_room.e_to)

  
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
print("traversal_path",traversal_path)
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

