# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidbst(node, low, high) -> bool: #helper function to keep track of low and high
            if not node: #if the node doesnt exist, it becomes true automatically
                return True
            
            if node.val <= low or node.val >= high: #if the value doesnt meet the boundaries either way, its false since you're updating the values on each computation
                return False
            
            return isValidbst(node.left, low, node.val) and isValidbst(node.right, node.val, high) #check both the left AND right side, updating the left side high to the prev val and right side low to the prev val
        
        return isValidbst(root, float("-inf"), float("inf")) #use helper starting with negative and positive infinity