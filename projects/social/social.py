import random


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

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f'User {i+1}')
        # Create friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id +1):
                possible_friendships.append((user_id, friend_id))
        random.shuffle(possible_friendships)
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])



    #BFS = Queue
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # Initialize
        queue = Queue()
        queue.enqueue([user_id])
        path = []
        print(94,self.friendships.keys())
        # Create Graph
            # If this doesn't work use .items() and refer to parent as f[0] and child 
            # as f[1]
        user = list(self.friendships.keys())
        friends = list(self.friendships.values())
        for u in user:
            if u not in self.users:
                self.add_user(u)
        for f in friends:
            print(104, f)
            if f not in self.users:
                
                self.add_user(f)
            self.add_friendship(u, f)

        # Use BFS
        while queue:
            p = queue.dequeue()
            path.append(p)
            node = path[-1]
            if node not in visited:
                if node in self.friendships:
                    return self.friendships[node]
                n = self.get_all_social_paths(node)
                for peeps in n:
                    new_path = list(path)
                    new_path.append(peeps)
                    queue.enqueue(new_path)
                    if peeps == user_id:
                        return new_path
                # visited.append(node) 
        
        # Check lengths
        # return the shorted length
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
