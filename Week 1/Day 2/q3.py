class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit, letter, result = [], [], []
        for i in range(len(logs)):
            value = logs[i].split(' ')
            if value[-1].isdigit():
                digit.append(i)
            else:
                letter.append([i])
                letter[-1].append(value[0])
                letter[-1].append("0".join(value[1:]))
        
        sortedletter = sorted(letter, key=lambda items: (items[2], items[1]))
        for i in range(len(sortedletter)):
            result.append(logs[sortedletter[i][0]])
        for i in range(len(digit)):
            result.append(logs[digit[i]])
        return result