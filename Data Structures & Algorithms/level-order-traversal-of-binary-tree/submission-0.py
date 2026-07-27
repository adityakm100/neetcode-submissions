# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] #out array 
        q = collections.deque() #double ended queue
        q.append(root) #adding the root to init

        while q: #while the queue can have values in it
            qLen = len(q) #this is how large the sublist can be 
            level = [] #sublist for this particular level since they have to be separate sublists
            for i in range(qLen): #going through only however many nodes need to go through for this level
                node = q.popleft() #popping from the left since queue is FIFO
                if node: #if the node exists
                    level.append(node.val) #add the value to the current sublist
                    q.append(node.left) #add its left 
                    q.append(node.right) #add its right
            if level: #if the level sublist has values
                res.append(level) #add this sublist to the main list
        return res #return result
            