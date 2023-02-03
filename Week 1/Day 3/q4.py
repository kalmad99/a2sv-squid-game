# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        row, col, hashmap = 0, 0, defaultdict(list)
        self.helper(root, 0, 0, hashmap)
        result = sorted(hashmap.items(), key=lambda items: items[0])
        answer = []
        for i in range(len(result)):
            temp = [x[1] for x in sorted(result[i][1], key=lambda items: (items[0], items[1]))]
            answer.append(temp)
        return answer

    def helper(self, node, row, col, hashmap):
        if not node:
            return

        hashmap[col].append((row, node.val))
        self.helper(node.left, row+1, col-1, hashmap)
        self.helper(node.right, row+1, col+1, hashmap)