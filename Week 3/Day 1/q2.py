class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        queue, visited = deque([(0,0,0)]), set([(0,0)])
        directions = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        while queue:
            x,y,step = queue.popleft()
            if (x,y) == (len(grid)-1,len(grid)-1):
                return step+1
            for direction in directions:
                newx, newy = x+direction[0], y+direction[1]
                if 0<=newx<len(grid) and 0<=newy<len(grid) and grid[newx][newy] == 0 and (newx, newy) not in visited:
                    visited.add((newx, newy))
                    queue.append((newx, newy, step+1))
        return -1