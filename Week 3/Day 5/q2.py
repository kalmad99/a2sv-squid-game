class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result, temp = [], []
        def helper(left, right, ctr):
            if ctr == n*2:
                if left == right:
                    result.append("".join(temp[:]))
                return 
            if left < n:
                temp.append('(')
                helper(left+1, right, ctr+1)
                temp.pop()
            if right < n and right < left: 
                temp.append(')')
                helper(left, right+1, ctr+1)
                temp.pop()
        helper(0, 0, 0)
        return result