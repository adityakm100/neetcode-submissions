# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: #if the tree doesnt exist then the subtree cannot exist
            return False
         
        check = False #default value
        if root.val == subRoot.val: #if the values ever match
            check = self.isSameTree(root, subRoot) #compute if its the same tree, and set that to check
        
        return check or (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)) #either the check matches or you keep checking subtrees as they exist, would lead to check1 or check2... or checkroot.