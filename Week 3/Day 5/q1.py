class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap, duplicate = defaultdict(lambda: 0), set()
        for i in range(len(s)):
            if s[i] in hashmap and s[i] not in duplicate:
                duplicate.add(s[i])
                del hashmap[s[i]]
            if s[i] not in duplicate:
                hashmap[s[i]] = i
        for i,j in hashmap.items():
            return j
        return -1