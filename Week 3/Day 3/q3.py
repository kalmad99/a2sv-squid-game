class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        return self.helper(0, 0, 0, s, memo)
    
    def helper(self, idx, left, right, s, memo):
        if (idx, left, right) in memo:
            return memo[(idx, left, right)]

        if idx == len(s):
            if left == right:
                return True
            return False
        
        result = False
        if right > left:
            return False
        if s[idx] == '(':
            result = result or self.helper(idx+1, left+1, right, s, memo)
        elif s[idx] == ')':
            result = result or self.helper(idx+1, left, right+1, s, memo)
        else:
            result = result or self.helper(idx+1, left, right+1, s, memo) or self.helper(idx+1, left+1, right, s, memo) or self.helper(idx+1, left, right, s, memo)
        memo[(idx, left, right)] = result
        return result
