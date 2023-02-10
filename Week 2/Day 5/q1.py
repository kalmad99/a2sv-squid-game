class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        first, second, result = 0, len(nums)-1, []
        while first <= second:
            if abs(nums[first]) >= abs(nums[second]):
                result.append(nums[first]**2)
                first += 1
            else:
                result.append(nums[second]**2)
                second -= 1
        return result[::-1]