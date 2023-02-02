class Solution:
    def numberOfWays(self, s: str) -> int:
        ones, zeros, result = [0], [0], 0
        for i in range(len(s)):
            if s[i] == '0':
                ones.append(ones[-1])
                zeros.append(zeros[-1] + 1)
            if s[i] == '1':
                ones.append(ones[-1] + 1)
                zeros.append(zeros[-1])

        for i in range(1, len(s)-1):
            if s[i] == '0':
                result += ones[i] * (ones[-1]-ones[i])
            else:
                result += zeros[i] * (zeros[-1]-zeros[i])
        return result