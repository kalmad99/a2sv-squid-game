class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result = 0
        for i in range(len(logs)):
            if len(logs[i]) >= 3:
                if logs[i][0] != '.':
                    result += 1
                else:
                    if result > 0:
                        result -= 1
            if len(logs[i]) == 2:
                if logs[i][0] != '.':
                    result += 1
        return result