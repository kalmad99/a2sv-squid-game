class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        merged, maxi = [], 0
        for i in range(len(scores)):
            merged.append((ages[i], scores[i]))
        merged = sorted(merged, key=lambda items: (items[0], items[1]))
            
        dp = [merged[i][1] for i in range(len(merged))]
        for i in range(1, len(merged)):
            for j in range(i):
                if merged[i][1] >= merged[j][1]:
                    dp[i] = max(dp[i], dp[j] + merged[i][1])
        return max(dp)