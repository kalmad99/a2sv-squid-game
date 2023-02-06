class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=lambda items:len(items))
        dp = [1 for i in words]
        for i in range(1, len(words)):
            for j in range(i):
                if len(words[i]) == len(words[j])+1:
                    first, second, error = 0, 0, 0
                    while first < len(words[j]):
                        if words[i][second] != words[j][first]:
                            if error == 0:
                                error += 1
                                second += 1
                            else:
                                break
                        else:
                            first += 1
                            second += 1
                    if first == len(words[j]):
                        dp[i] = max(dp[i], dp[j]+1)
        return max(dp) 