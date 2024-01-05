class HashTable:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

    def _get_hash(self, key):
        return hash(key) % self.size

    def print_hash(self):
        for k, v in enumerate(self.map):
            print(f"{k} : {v}")

    def set(self, key, value):
        index = self._get_hash(key)
        if self.map[index] is None:
            self.map[index] = []
        self.map[index].append([key, value])

    def get(self, key):
        index = self._get_hash(key)
        if self.map[index] is not None:
            for i in range(len(self.map[index])):
                if self.map[index][i][0] == key:
                    return self.map[index][i][1]
        return None


my_hash = HashTable()
my_hash.set("messi", 10)
my_hash.set("MJF", 13)
my_hash.print_hash()
print(my_hash.get("MJF"))
