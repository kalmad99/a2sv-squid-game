class Solution:
    def racecar(self, target: int) -> int:
        queue, result, visited = deque([(0,1,0)]), float('inf'), set()
        
        while queue:
            pos, speed, moves = queue.popleft()
            if pos == target:
                result = min(result,moves)
                continue
            if (pos, speed) not in visited:
                visited.add((pos, speed))
                if moves > result:
                    continue
                queue.append((pos+speed, speed*2, moves+1))
                if ((pos+speed > target and speed > 0) or (pos+speed<target and speed<0)):
                    queue.append((pos, (-1*speed)/abs(speed), moves+1))
        return result