class HashTable:
    def __init__(self):
        self.collection = dict()

    def hash(self, key):
        return sum([ord(char) for char in key])

    def add(self, key, value):
        pass

    def remove(self, key, value):
        pass

    def lookup(self, key):
        pass


key = 'golf'
hashkey = HashTable().hash(key)

print(f"{key}: {hashkey}")