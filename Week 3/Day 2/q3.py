class Solution:
    def minimumDeletions(self, s: str) -> int:
        a, b = [0], [0]
        for i in range(len(s)):
            if s[i] == 'b':
                a.append(a[-1] + 1)
            else:
                a.append(a[-1])

        for i in range(len(s)-1, -1, -1):
            if s[i] == 'a':
                b.append(b[-1] + 1)
            else:
                b.append(b[-1])
        b = b[::-1]

        result = len(s)

        for i in range(1, len(a)):
            result = min(result, a[i-1] + b[i])
        return result