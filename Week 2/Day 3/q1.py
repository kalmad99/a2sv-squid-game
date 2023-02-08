class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3:
            return nums[-1]
        heap = []
        for i in range(len(nums)):
            heappush(heap, nums[i])
            if len(heap) > 3:
                heappop(heap)
        return heappop(heap)
