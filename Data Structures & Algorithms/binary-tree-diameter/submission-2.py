# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: #ALWAYS NEED THIS BASE CASE
            return 0
    
        def dfs(node: Optional[TreeNode]) -> tuple[int, int]: #helper function, returns a pair of height at node, curr_max diameter at this node
            if not node: #ALWAYS NEED THIS BASE CASE
                return 0, 0
            
            left_height, left_diam = dfs(node.left) #compute height and max diameter of left side
            right_height, right_diam = dfs(node.right) #compute height and max diameter of right side

            curr_height = 1 + max(left_height, right_height) #compute the height at this node, same formula as always, 1 + max of the left and right side is the depth cause +1 is the root
            max_diam = left_height + right_height #max diameter from this node

            curr_max_diam = max(max_diam, left_diam, right_diam) #current max diameter could be from this node, or from nodes down left and right, so compute max of all numbers

            return curr_height, curr_max_diam #return current iteration of height and max diameter from this particular node argument
        
        _ , diam = dfs(root) #diam here would be max theoretical diam since you're passing the root in

        return diam #return

            