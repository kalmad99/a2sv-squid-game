class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed, result = sorted(changed, reverse=True), []
        hashmap = Counter(changed)
        for i, j in hashmap.items():
            if i == 0:
                if j % 2 != 0:
                    return []
                result.extend([0]*(j//2))
            else:
                if j > 0:
                    if i%2 != 0 or i//2 not in hashmap or hashmap[i//2] < j:
                        return []
                    hashmap[i//2] -= j
                    result.extend([i//2]*j)
        return result