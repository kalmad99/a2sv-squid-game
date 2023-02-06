class DetectSquares:

    def __init__(self):
        self.row = defaultdict(list)
        self.check = defaultdict(lambda: 0)

    def add(self, point: List[int]) -> None:
        self.check[(point[0], point[1])] += 1
        self.row[point[1]].append(point[0])

    def count(self, point: List[int]) -> int:
        result = 0
        for i in range(len(self.row[point[1]])):
            if self.row[point[1]][i] != point[0]: 
                diff = abs(point[0] - self.row[point[1]][i])
                if (self.row[point[1]][i], point[1]-diff) in self.check and (point[0], point[1]-diff) in self.check:
                    result += self.check[(self.row[point[1]][i], point[1]-diff)]*self.check[(point[0], point[1]-diff)]
                if (self.row[point[1]][i], point[1]+diff) in self.check and (point[0], point[1]+diff) in self.check:
                    result += self.check[(self.row[point[1]][i], point[1]+diff)]*self.check[(point[0], point[1]+diff)]
        return result

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)