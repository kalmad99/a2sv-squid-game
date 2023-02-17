class LRUCache:

    def __init__(self, capacity: int):
        self.timestamp, self.value, self.array = {}, {}, deque()
        self.time, self.cap = 1, capacity

    def get(self, key: int) -> int:
        if key in self.timestamp:
            self.timestamp[key] = self.time
            self.array.append((key, self.time))
        self.time += 1
        return self.value[key] if key in self.value else -1

    def put(self, key: int, value: int) -> None:
        self.array.append((key, self.time))
        self.timestamp[key] = self.time
        self.value[key] = value
        while len(self.timestamp) > self.cap:
            if self.array[0][1] == self.timestamp[self.array[0][0]]:
                del self.timestamp[self.array[0][0]]
                del self.value[self.array[0][0]]
            self.array.popleft()
        self.time += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)