class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        total, sum, result = defaultdict(lambda: 0), 0, 0
        total[0] = 1
        for num in nums:
            sum += num
            if sum%k in total:
                result += total[sum%k]
            total[sum%k] += 1
        return result