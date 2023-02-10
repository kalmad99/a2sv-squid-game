class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        hashmap, result = defaultdict(lambda: 0), 0
        for num in nums:
            hashmap[num] += 1
        for i, j in hashmap.items():
            prefix, suffix = target[:len(i)], target[len(i):] 
            if i == prefix and suffix in hashmap:
                if suffix == prefix:
                    result += (hashmap[suffix]*(hashmap[suffix]-1))
                else:
                    result += hashmap[prefix]*hashmap[suffix]
        return result
