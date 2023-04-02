# 705. Design HashSet

# Design a HashSet without using any built-in hash table libraries.

# Implement MyHashSet class:

# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

class MyHashSet:

    def __init__(self):
        self.array = [[] for _ in range(100000)]

    def add(self, key: int) -> None:
        subkey = key % 1000
        if not self.contains(key):
            self.array[subkey].append(key)

    def remove(self, key: int) -> None:
        subkey = key % 1000
        if self.contains(key):
            self.array[subkey].remove(key)

    def contains(self, key: int) -> bool:
        subkey = key % 1000
        return key in self.array[subkey]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)