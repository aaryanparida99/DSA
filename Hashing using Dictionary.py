class HashTable:  
    def __init__(self):
        self.MAX = 10
        ## List Comprehension
        self.arr = [None for i in range(self.MAX)]

    ## Method to calculate the hash function for a given value 
    def get_hash(self, key):
        hash = 0
        for char in key:
            ## ord function in python helps us to get ascii value of 
            ## any character
            hash += ord(char)
        return hash % self.MAX
    
    ## Method definition of standard operators as functions in Python
    ## getitem - to fetch the value of given index inside hash table
    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]
    ## setitem - to set the value corresponding to key inside hash table
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val    
    ## delitem - to delete the values inside the hash table for a given key  
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None