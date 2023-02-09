class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = set()
        if 4 <= len(s) <= 12:
            self.helper(0, s, 0, [], result)
        return result
        
    def helper(self, idx, s, ctr, temp, result):
        if idx >= len(s):
            if ctr == 4:
                result.add(".".join(temp[:]))
            return

        for i in range(3):
            val = s[idx:idx+i+1]
            if (i != 0 and val[0] == '0'):
                return
            if 0 <= int(val) <= 255:      
                temp.append(s[idx:idx+i+1])
                self.helper(idx+i+1, s, ctr+1, temp, result)
                temp.pop()
            