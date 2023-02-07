class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            heappush(heap, nums[i])
            if len(heap) > k:
                heappop(heap)
        return heap[0]