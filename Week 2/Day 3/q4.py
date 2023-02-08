class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        buses, possible, start, end = defaultdict(list), defaultdict(set), None, None
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                if routes[i][j] == source:
                    start = i
                if routes[i][j] == target:
                    end = i
                buses[routes[i][j]].append(i)

        for i in range(len(routes)):
            for j in range(len(routes[i])):
                for k in buses[routes[i][j]]:
                    possible[i].add(k)
        
        queue, visited, mini = deque(), set(), float('inf')
        for i in buses[source]:
            queue.append((i, 1))
        while queue:
            bus, step = queue.popleft()
            if step > mini:
                continue
            visited.add(bus)
            if bus in buses[target]:
                mini = min(mini, step)
                continue
            for nei in possible[bus]:
                if nei not in visited:
                    queue.append((nei, step+1))
        return mini if mini != float('inf') else -1