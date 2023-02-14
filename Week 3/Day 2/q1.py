class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        for i in range(n//2,0,-1):
            result.append(i)
            result.append(-i)
        if n%2!=0:
            result.append(0)
        return result