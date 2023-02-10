class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        minheap, maxheap = [], []
        for num in nums1+nums2:
            heappush(minheap, num)

        while len(minheap) > len(maxheap):
            heappush(maxheap, -1*heappop(minheap))
        return -maxheap[0] if len(maxheap) > len(minheap) else (-maxheap[0]+minheap[0])/2