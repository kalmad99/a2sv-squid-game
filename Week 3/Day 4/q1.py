class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        idx, result = len(s)-1, 0
        while idx > -1:
            if idx-1 > -1:
                if ((s[idx] == 'V' or s[idx] == 'X') and s[idx-1] == 'I') or ((s[idx] == 'L' or s[idx] == 'C') and s[idx-1] == 'X') or ((s[idx] == 'D' or s[idx] == 'M') and s[idx-1] == 'C'):
                    result += hashmap[s[idx]]-hashmap[s[idx-1]]
                    idx -= 1
                else:
                    result += hashmap[s[idx]]
            else:
                result += hashmap[s[idx]]
            idx -= 1
        return result