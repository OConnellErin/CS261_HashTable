# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# Erin O'Connell


class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.data = [ [] for i in range(size) ]

    def __setitem__(self, key, value):
        index =self.hash(key)
        pairs = self.data[index]
        for pair in pairs:
            if pair[0] ==key:
                pair[1] = value 
                return        
        self.data[index].append([key,value])                

    def __getitem__(self,key):
        index =self.hash(key)
        pairs = self.data[index]
        for pair in pairs:
            if pair[0] ==key:
                return pair[1]
        return None            

    def hash(self, key):
        return hash(key) % self.size
    
    def delete(self, key):
        index = self.hash(key)
        pairs = self.data[index]
        for pair in pairs: 
            if pair[0] == key:
                pair[0]=[]
                pair[1]=[]

    def clear(self, size=3):
        self.data = [ [] for i in range(size) ]
    
    def keys(self):
        keys = []
        for index in self.data:
            for pair in index:
                keys.append(pair[0])
        return keys        

    def values(self):
        values = []
        for index in self.data:
            for pair in index:
                values.append(pair[1])
        return values        
