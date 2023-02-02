class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        total, result = 0, 0
        for i in range(len(nums)):
            if nums[i] - total > 0:
                result += 1
                total += nums[i] - total
        return result