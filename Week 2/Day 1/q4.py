class Solution:
    def racecar(self, target: int) -> int:
        queue, visited = deque([(0, 1, 0)]), set()
        while queue:
            pos, spe, ctr = queue.popleft()
            if pos == target:
                return ctr
            if (pos, spe) not in visited:
                visited.add((pos,spe))
                queue.append((pos+spe, spe*2, ctr+1))
                if pos+spe > target and spe > 0 or pos+spe < target and spe < 0:
                    queue.append((pos, -1*spe/abs(spe), ctr+1))