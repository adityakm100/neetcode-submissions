# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root: #if root still doesnt exist, return None
            return None
        
        if root.val < p.val and root.val < q.val: #if the value of the root is less for both p and q, p and q is greater, and in a BST, the greater values are to the right of the root
            return self.lowestCommonAncestor(root.right, p, q) #check the right
        elif root.val > p.val and root.val > q.val: #if the value of the root is greater for both p and q, then p and q is less, and in a BST, the less values are to the left of the root
            return self.lowestCommonAncestor(root.left, p, q) #check the left
        else: #this means that there is an in between
            return root #ANS