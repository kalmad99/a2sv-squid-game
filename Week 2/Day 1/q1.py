class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        result = 0
        for i in range(len(words)):
            first, second = 0, 0
            while first < len(words[i]) and second < len(pref):
                if pref[second] == words[i][first]:
                    first += 1
                    second += 1
                else:
                    break
            if second == len(pref):
                result += 1
        return result