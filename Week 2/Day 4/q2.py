class Solution:
    def maximumSwap(self, num: int) -> int:
        numstring, result = list(str(num)), [num]
        for i in range(len(numstring)-1):
            for j in range(i+1, len(numstring)):
                number = numstring[:]
                temp = number[i]
                number[i] = number[j]
                number[j] = temp
                result.append(int("".join(number)))
        return sorted(result)[-1]