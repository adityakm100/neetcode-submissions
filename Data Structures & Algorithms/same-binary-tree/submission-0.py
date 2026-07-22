# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: #both nodes don't exist, so its true since they both dont exist
            return True
        
        if not p or not q: #this means one exists and one doesn't, so its false because they're not the same
            return False
        
        if p.val != q.val: #obvious check for falseness
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) #checks the left and right side with the base cases above to break out, they both have to work so thats why its and