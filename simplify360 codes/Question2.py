class SocialNetwork:
    def __init__(self):
        self.network = {}
    def add_friendship(self, person, friend):
        if person not in self.network:
            self.network[person] = []
        if friend not in self.network:
            self.network[friend] = []
        self.network[person].append(friend)
        self.network[friend].append(person)
    def get_friends(self, person):
        return self.network.get(person, [])
    def common_friends(self, person1, person2):
        friends1 = set(self.get_friends(person1))
        friends2 = set(self.get_friends(person2))
        return list(friends1.intersection(friends2))
    def nth_connection(self, start, end):
        from collections import deque
        if start == end:
            return 0
        visited = set()
        queue = deque([(start, 0)])
        while queue:
            current, depth = queue.popleft()
            if current not in visited:
                visited.add(current)
                for friend in self.get_friends(current):
                    if friend == end:
                        return depth + 1
                    queue.append((friend, depth + 1))
        return -1
# Example usage
if __name__ == "__main__":
    sn = SocialNetwork()
    sn.add_friendship("Alice", "Bob")
    sn.add_friendship("Bob", "Janice")
    sn.add_friendship("Alice", "Charlie")
    sn.add_friendship("Charlie", "Dave")

    print("Friends of Alice:", sn.get_friends("Alice"))  
    print("Friends of Bob:", sn.get_friends("Bob"))  
    print("Common friends of Alice and Bob:", sn.common_friends("Alice", "Bob")) 
    print("2nd connection (Alice, Janice):", sn.nth_connection("Alice", "Janice")) 
    print("1st connection (Alice, Bob):", sn.nth_connection("Alice", "Bob")) 
    print("No connection (Alice, Dave):", sn.nth_connection("Alice", "Dave"))