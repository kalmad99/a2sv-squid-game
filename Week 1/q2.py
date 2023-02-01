class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        newmat = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        result = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        newmat[0][0] = mat[0][0]
        for i in range(1, len(mat)):
            newmat[i][0] = newmat[i-1][0] + mat[i][0]
        for i in range(1, len(mat[0])):
            newmat[0][i] = newmat[0][i-1] + mat[0][i]
        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):
                newmat[i][j] = mat[i][j] - newmat[i-1][j-1] + newmat[i][j-1] + newmat[i-1][j]
                
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                startx, starty, endx, endy = max(i-k, 0), max(j-k, 0), min(i+k, len(mat)-1), min(j+k, len(mat[0])-1)
                rowsum, colsum, lone = 0, 0, 0
                if 0 <= startx-1 < len(mat) and 0 <= starty-1 < len(mat[0]):
                    lone = newmat[startx-1][starty-1]
                if 0 <= endx < len(mat) and 0 <= starty-1 < len(mat[0]):
                    rowsum = newmat[endx][starty-1]
                if 0 <= startx-1 < len(mat) and 0 <= endy < len(mat[0]):
                    colsum = newmat[startx-1][endy]
                
                result[i][j] = newmat[endx][endy] + lone - rowsum - colsum
        return result