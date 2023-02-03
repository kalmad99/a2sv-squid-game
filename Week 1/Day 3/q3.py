class Solution:

    def __init__(self, w: List[int]):
        self.total = sum(w)
        self.prefix = [w[0]]
        for i in range(1, len(w)):
            self.prefix.append(self.prefix[-1] + w[i])

    def pickIndex(self) -> int:
        rand = random.randint(1, self.total)
        idx = bisect.bisect_left(self.prefix, rand)
        return idx

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()