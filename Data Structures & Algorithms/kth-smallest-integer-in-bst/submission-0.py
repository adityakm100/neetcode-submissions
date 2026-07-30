# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0 #global variables to keep track of how many nodes have been visited
        self.result = None #result stored here
        def helper(node: Optional[TreeNode]): #helper for dfs
            if not node or self.result is not None: #if the node doesnt exist or a result has already been found, no need to go into this helper, just return
                return
            
            helper(node.left) #keep going down the left side

            self.count += 1 #increment the count of the current node being visited by 1
            if self.count == k: #if this reaches k, as expected, set the k to be the current node and return
                self.result = node.val
                return
            
            helper(node.right) #now go down the right

            #THIS IS AN INORDER TRAVERSAL, LEFT -> NODE -> RIGHT, SINCE THE LEFT VALUES ARE SMALLER, WE WANT TO START THERE SINCE WE ARE LOOKING FOR THE Kth SMALLEST INTEGER IN BST
        
        helper(root) #run the helper starting from the root
        return self.result #return the stored result
