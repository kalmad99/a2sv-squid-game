class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        instructions = 4*instructions
        directions = {"N": ["W", "E"], "W": ["S", "N"], "E": ["N", "S"], "S": ["E", "W"]}
        direction, start = "N", [0,0]
        move = {"N": (1,0), "E": (0,1), "W": (0,-1), "S": (-1, 0)}
        for i in range(len(instructions)):
            if instructions[i] == 'G':
                start[0] += move[direction][0]
                start[1] += move[direction][1]
            elif instructions[i] == 'L':
                direction = directions[direction][0]
            else:
                direction = directions[direction][1]
        return start == [0,0]