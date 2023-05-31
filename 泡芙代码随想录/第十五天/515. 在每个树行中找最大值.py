# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        temp_result = []
        self.recur(root,0,temp_result)
        result = []
        for i in range(len(temp_result)):
            result.append(max(temp_result[i]))
        return result
    def recur(self, node, level, result):
        if not node:
            return result
        if len(result) == level:
            result.append([])
        result[level].append(node.val)
        self.recur(node.left, level+1, result)
        self.recur(node.right, level+1, result)