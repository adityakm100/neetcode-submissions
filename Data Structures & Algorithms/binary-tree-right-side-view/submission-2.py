# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: #base case for empty root
            return [] #return empty array
        
        res = [] #output array

        q = collections.deque() #initializing a deque for BFS
        q.append(root) #adding the root as initializing value

        while q: #while the queue still exists
            lenQ = len(q) #length of the level we care about (the remaining nodes in the queue)
            for i in range(lenQ): #iterate through only these nodes since queue is FIFO
                node = q.popleft() #pop the oldest node from queue
                
                if i == lenQ - 1: #if its the last node in this level, store it in the result since its the rightmost node in this level of the queue
                    res.append(node.val) #save it
                if node.left: #if the left value exists, add it to the queue
                    q.append(node.left)
                if node.right: #same with right side
                    q.append(node.right)
        return res #return