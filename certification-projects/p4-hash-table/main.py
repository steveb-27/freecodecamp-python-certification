class HashTable:
    def __init__(self):
        self.collection = dict()

    def hash(self, key):
        return sum([ord(char) for char in key])

    def add(self, key, value):
        hashkey = self.hash(key)
        if hashkey not in self.collection:
            self.collection[hashkey] = dict()
        self.collection[hashkey][key] = value

    def remove(self, key):
        hashkey = self.hash(key)
        if hashkey in self.collection:
            if key in self.collection[hashkey]:
                del self.collection[hashkey][key]
                if len(self.collection[hashkey]) == 0:
                    del self.collection[hashkey]

    def lookup(self, key):
        hashkey = self.hash(key)
        if hashkey in self.collection.keys() and key in self.collection[hashkey]:
            return self.collection[hashkey][key]
        return None


key = 'golf'
hashtable = HashTable()
hashtable.add('rose', 'flower')
hashkey = hashtable.hash(key)

print(f"{key}: {hashkey}")
print(hashtable.collection)