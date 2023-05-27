import random


class ChainingHash:
    def __init__(self, size):
        self.__capacity = size
        self.__Table = []
        for _ in range(self.__capacity):
            self.__Table.append([])
        self.collisions = 0
        self.collision_index = []

    def __hash_function(self, key):
        return key % self.__capacity

    def insert_chaining(self, key):
        index = self.__hash_function(key)
        if len(self.__Table[index]) > 0:
            self.collisions += 1
        self.__Table[index].append(key)

    def reset(self):
        self.__Table = []
        for _ in range(self.__capacity):
            self.__Table.append([])
        self.collisions = 0


class LinearHash:
    def __init__(self, size):
        self.__capacity = size
        self.__Table = [None] * self.__capacity
        self.collisions = 0

    def __hash_function(self, key):
        return key % self.__capacity

    def insert_linear(self, key):
        index = self.__hash_function(key)
        if self.__Table[index] is not None:
            self.collisions += 1
            while self.__Table[index] is not None:
                index = (index + 1) % self.__capacity
        self.__Table[index] = key

    def reset(self):
        self.__Table = [None] * self.__capacity
        self.collisions = 0


arrays = []
for _ in range(10):
    array = []
    for _ in range(5000):
        number = random.randint(0, 100000)
        array.append(number)
    arrays.append(array)

# chaining
chaining_hash = ChainingHash(6001)
chaining_collisions = []
for i in range(10):
    for number in arrays[i]:
        chaining_hash.insert_chaining(number)
    chaining_collisions.append(chaining_hash.collisions)
    chaining_hash.reset()
chaining_max = max(chaining_collisions)
chaining_min = min(chaining_collisions)
chaining_average = sum(chaining_collisions)/10
print(chaining_collisions)
print(chaining_max)
print(chaining_min)
print(chaining_average)

# linear
linear_hash = LinearHash(6001)
linear_collisions = []
for i in range(10):
    for number in arrays[i]:
        linear_hash.insert_linear(number)
    linear_collisions.append(linear_hash.collisions)
    linear_hash.reset()
linear_max = max(linear_collisions)
linear_min = min(linear_collisions)
linear_average = sum(linear_collisions)/10
print(linear_collisions)
print(linear_max)
print(linear_min)
print(linear_average)
# print arrays
"""for i, array in enumerate(arrays):
    print(f"Array {i + 1}: {array}")"""
