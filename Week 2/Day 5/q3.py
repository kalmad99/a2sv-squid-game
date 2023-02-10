class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        newimg, res = [[0 for _ in range(len(img1)*3)] for _ in range(len(img1)*3)], 0
        for i in range(len(img1), len(img1)*2):
            for j in range(len(img1), len(img1)*2):
                newimg[i][j] = img1[i-len(img1)][j-len(img1)]
        for i in range(len(newimg)-len(img1)):
            for j in range(len(newimg)-len(img1)):
                board = [row[j:j+len(img1)] for row in newimg[i:i+len(img1)]]
                temp = self.check(board, img2)
                res = max(res, temp)
        return res
                
    def check(self, first, second):
        counter = 0
        for i in range(len(first)):
            for j in range(len(first)):
                if first[i][j] == second[i][j] == 1:
                    counter += 1
        return counter