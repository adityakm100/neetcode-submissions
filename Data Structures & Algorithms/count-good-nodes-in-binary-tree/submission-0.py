# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def goodNodesHelper(self, root: TreeNode, maxValue: int) -> int:
        if not root:
            return 0
            
        if root.val >= maxValue:
            return 1 + self.goodNodesHelper(root.left, root.val) + self.goodNodesHelper(root.right, root.val)
        else:
            return self.goodNodesHelper(root.left, maxValue) + self.goodNodesHelper(root.right, maxValue)



    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        maxVal = root.val
        
        return 1 + self.goodNodesHelper(root.left, maxVal) + self.goodNodesHelper(root.right, maxVal)