class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        result = True
        while start < end:
            if s[start] != s[end]:
                result = False
                break
            start += 1
            end -= 1
        return result | self.helper(start+1, end, s) | self.helper(start, end-1, s)

    def helper(self, start, end, s):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True