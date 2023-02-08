class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        hashmap, answer = defaultdict(list), []
        for i in range(len(equations)):
            hashmap[equations[i][0]].append((equations[i][1], values[i]))
            hashmap[equations[i][1]].append((equations[i][0], 1/values[i]))

        for i in range(len(queries)): 
            result = [-1]
            if queries[i][0] not in hashmap or queries[i][1] not in hashmap:
                answer.append(-1)
            else:
                self.helper(queries[i][0], queries[i][1], hashmap, set(), 1, result)
                answer.append(result[0])
        return answer

    def helper(self, curr, end, hashmap, visited, temp, result):
        if curr == end:
            result[0] = temp
            return
        visited.add(curr)
        for nei, val in hashmap[curr]:
            if nei not in visited:
                self.helper(nei, end, hashmap, visited, temp*val, result)
                if result[0] != -1:
                    return

