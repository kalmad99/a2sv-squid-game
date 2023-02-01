class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        combined = [(plantTime[i], growTime[i]) for i in range(len(plantTime))]
        combined = sorted(combined, key=lambda items: -items[1])
        time, maxEnd = 0, 0
        for i in range(len(combined)):
            time += combined[i][0]
            maxEnd = max(maxEnd, time+combined[i][1])
        return maxEnd