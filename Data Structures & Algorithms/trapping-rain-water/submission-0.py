class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: #have to check this edge case on this code
            return 0
        
        #REMINDER: EQUATION BEING ADAPTED IS: sum of min(maxLeft, maxRight) - heights[i] at each position

        l = 0
        r = len(height) - 1
        maxl = height[l] #need to store the absolute max of left side, updated on every pointer move, helps with the algorithm compute
        maxr = height[r]
        watr = 0

        while l < r:
            if maxl < maxr: #only move the respective pointer, if leftMax is lower than rightMax, we know that leftMax or the left side is the bottleneck in a min equation, so we would move that in to try to find something new (find a new bottleneck so to speak)
                l += 1
                maxl = max(maxl, height[l]) #update the max per iteration, wont change if it isn't max
                watr += maxl - height[l] #we don't need to make any checks on if this is negative because we update the maxleft before ever doing this computation, so the two cases would be that the max did get updated in which case the water gets 0 (basically number minus itself) added to it, or that the max didn't get updated and there is actually a potential number that can be added to the water
            else:
                r -= 1
                maxr = max(maxr, height[r])
                watr += maxr - height[r] #we only need to check maxr - height[r] instead of doing the whole min calculation again because the condition for entering the loop is that maxr is less than maxl, so we would only use that one as a check for the equation
        return watr
