# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: #base case
            return None
        
        new_right = self.invertTree(root.left) #recursive call to go all the way down left and switch it to right
        new_left = self.invertTree(root.right) #same recursive call here
        root.left = new_left #setting
        root.right = new_right #same here

        return root