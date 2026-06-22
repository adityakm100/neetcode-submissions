class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l, r = 0, 0
        q = collections.deque() #way in python to initialize a deque, will contain indices because it saves memory

        while r < len(nums): #check to stay in bounds
            while q and nums[q[-1]] < nums[r]: #while the queue has values and the topmost value on the queue is less than the value being inserted, we would pop to preserve the monotonic decreasing nature of the deque
                q.pop() #pop from the right while the condition isn't preserved, since that's where the small numbers are
            q.append(r) #only after that check to preserve the condition of the deque can we add the new index

            if l > q[0]: #if the left pointer has passed the topmost value of the deque, then we don't care about the value in that deque for this window, so we can pop from the left
                q.popleft() #pop from the left
            
            if r + 1 >= k: #since we also initialize right to 0 even though it should start from past k, we add this check to not add anything that is not in our first window of k
                res.append(nums[q[0]])
                l += 1 #increment left once the conditions of the question are active
            r += 1 #always increment right
        return res
