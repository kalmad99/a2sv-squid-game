class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result, total = nums[0], nums[0]
        for i in range(1, len(nums)):
            if total + nums[i] >= nums[i]:
                total += nums[i]
            else:
                total = nums[i]
            result = max(result, total)
        return result