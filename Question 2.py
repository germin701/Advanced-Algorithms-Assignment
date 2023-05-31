import random


class HashTable:
    def __init__(self, size):
        self.__capacity = size
        self.__Table = []
        self.collisions = 0

    def chaining_table(self):
        # Append empty list in self.__Table by follow the size of the hash table
        for _ in range(self.__capacity):
            self.__Table.append([])

    def linear_table(self):
        # Declare every index of hash table to None
        self.__Table = [None] * self.__capacity

    def __hash_function(self, key):
        return key % self.__capacity

    def insert_chaining(self, key):
        index = self.__hash_function(key)
        # Verify the index of table is not empty
        if len(self.__Table[index]) > 0:
            self.collisions += 1
        self.__Table[index].append(key)

    def insert_linear(self, key):
        index = self.__hash_function(key)
        # Loop when the index of table is not empty
        while self.__Table[index] is not None:
            self.collisions += 1
            index = (index + 1) % self.__capacity
        self.__Table[index] = key

    def reset_chaining_table(self):
        self.__Table = []
        for _ in range(self.__capacity):
            self.__Table.append([])
        self.collisions = 0

    def reset_linear_table(self):
        self.__Table = [None] * self.__capacity
        self.collisions = 0

# Create an array to store 10 set of random generated number
arrays = []
for _ in range(10):
    array = []
    for _ in range(5000):
        number = random.randint(0, 100000)
        array.append(number)
    arrays.append(array)

# Chaining
chaining_hash = HashTable(6001)
chaining_hash.chaining_table()
# An array to store the collision occurred in 10 execution
chaining_collisions = []
# For loop to execute 10 time
for i in range(10):
    # For loop to insert a set of number from the array
    for number in arrays[i]:
        chaining_hash.insert_chaining(number)
    chaining_collisions.append(chaining_hash.collisions)
    chaining_hash.reset_chaining_table()
chaining_max = max(chaining_collisions)
chaining_min = min(chaining_collisions)
chaining_average = sum(chaining_collisions) / 10

# Linear Probing
linear_hash = HashTable(6001)
linear_hash.linear_table()
# An array to store the collision occurred in 10 execution
linear_collisions = []
# For loop to execute 10 time
for i in range(10):
    # For loop to insert a set of number from the array
    for number in arrays[i]:
        linear_hash.insert_linear(number)
    linear_collisions.append(linear_hash.collisions)
    linear_hash.reset_linear_table()
linear_max = max(linear_collisions)
linear_min = min(linear_collisions)
linear_average = sum(linear_collisions) / 10

# Print out the output of each of the execution
for i in range(10):
    print("Execution " + str(i + 1) + "\nThe number of collision occurred in chaining is " + str(chaining_collisions[i])
          + "\nThe number of collision occurred in linear probing is " + str(linear_collisions[i]) + "\n")

# Print out the final table
print("\t\t\t\t\t\tAverage Cost\n\t\t  Chaining\t\t\t|\t\tOpen Addressing\nMinimum | Maximum | Average | Minimum | "
      "Maximum | Average\n  " + str(chaining_min) + "\t|\t" + str(chaining_max) + "  |\t" + str(chaining_average) +
      "\t|  " + str(linear_min) + "  |  " + str(linear_max) + "\t| " + str(linear_average))
