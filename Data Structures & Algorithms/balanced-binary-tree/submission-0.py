# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(node: Optional[TreeNode]) -> tuple[int, bool]:
            if not node:
                return 0, True
            
            left_height, left = dfs(node.left)
            right_height, right = dfs(node.right)

            curr_height = 1 + max(left_height, right_height)

            false = True

            if abs(left_height - right_height) > 1 or not left or not right:
                false = False
            
            return curr_height, false
        
        _ , true = dfs(root)
        return true