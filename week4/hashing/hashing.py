class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self,key):
        # Insert your hashing function code
        keystr = str(key)
        hashVal = 0
        for ch in str(keystr):
            hashVal += ord(ch)
        return (hashVal % self.size)

    def rehash(self,key):
        # Insert your secondary hashing function code
        keystr = str(key)
        hashVal = 0
        count = 0
        for ch in str(keystr):
            count += 1
            hashVal += ord(ch) + count
        return (hashVal % self.size)

    def put(self,key,data):
        # Insert your code here to store key and data 
        newPos = self.hashfunction(key)
        while self.slots[newPos] and self.data[newPos]:
            newPos = self.rehash(key)
            break
        self.data[newPos] = data
        self.slots[newPos] = key

    def get(self,key):
        # Insert your code here to get data by key
        return self.data[self.hashfunction(key)]

    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        self.put(key,data)


H = HashTable()
H[69] = 'A'

# Store remaining input data
H.put(66, 'B')
H.put(80, 'C')
H.put(35, 'D')
H.put(18, 'E')
H.put(52, 'F')
H.put(89, 'G')
H.put(70, 'H')
H.put(12, 'I')

# print the slot values
print(H.slots)

# print the data values
print(H.data)

# print the value for key 52
print(H.get(52))
