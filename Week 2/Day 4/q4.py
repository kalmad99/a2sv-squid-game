class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.helper(nums, k) - self.helper(nums, k-1)

    def helper(self, nums, k):
        left, right, counter, result = 0, 0, defaultdict(lambda: 0), 0
        while right < len(nums):
            counter[nums[right]] += 1
            while len(counter) > k:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
            right += 1
            result += right-left            
        return result