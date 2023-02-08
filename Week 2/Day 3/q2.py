class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        hashmap = defaultdict(list)
        for i in range(len(adjacentPairs)):
            hashmap[adjacentPairs[i][0]].append(adjacentPairs[i][1])
            hashmap[adjacentPairs[i][1]].append(adjacentPairs[i][0])

        start = None
        for i,j in hashmap.items():
            if len(j) == 1:
                start = i
                break

        result, visited = [], set()
        
        def helper(curr):
            result.append(curr)
            visited.add(curr)
            for nei in hashmap[curr]:
                if nei not in visited:
                    helper(nei)

        helper(start)
        return result