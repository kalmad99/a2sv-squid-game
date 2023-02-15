class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        possible, hashmap, ctr = set(), defaultdict(list), 0
        while ctr < sqrt(max(nums))+1:
            possible.add(ctr**2)
            ctr += 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    if nums[i] + nums[j] in possible:
                        hashmap[i].append(j)

        result, start = set(), set()
        for i in list(hashmap.keys()):
            if nums[i] not in start:
                visited = set((nums[i], 0))
                unique= set([i])
                self.helper(i, hashmap, nums, visited, unique, [nums[i]], result)
                start.add(nums[i])
        return len(result)

    def helper(self, idx, hashmap, nums, visited, unique, temp, result):
        if len(temp) == len(nums):
            val = tuple(temp) 
            if val not in result:
                result.add(val)
            return
        for nei in hashmap[idx]:
            if nei not in unique:
                unique.add(nei)
                temp.append(nums[nei])
                if tuple(temp) not in visited:
                    visited.add(tuple(temp))
                    self.helper(nei, hashmap, nums, visited, unique, temp, result)
                temp.pop()
                unique.remove(nei)