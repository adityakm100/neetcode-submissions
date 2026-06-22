class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l, r = 0, k
        while r <= len(nums):
            max_heap = [-x for x in nums[l:r]]
            heapq.heapify(max_heap)
            res.append(-max_heap[0])
            l += 1
            r += 1
        return res