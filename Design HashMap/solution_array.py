class MyHashMap:

    def __init__(self):
        self.map = [0]*1000001

    def put(self, key: int, value: int) -> None:
        self.map[key] = value + 1

    def get(self, key: int) -> int:
        return self.map[key] - 1

    def remove(self, key: int) -> None:
        self.map[key] = 0


map = MyHashMap()
map.put(1, 1)
map.put(2, 2)
print(map.get(1))