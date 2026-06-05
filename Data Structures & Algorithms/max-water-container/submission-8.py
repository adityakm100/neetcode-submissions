class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 #left pointer
        right = len(heights) - 1 #right pointer
        high = 0 #max to be returned

        while (left < right): #two pointer stuff
            curMax = min(heights[left], heights[right]) * (right - left) #compute the max with this iteration of left and right pointer
            high = max(high, curMax) #this got rid of my original idea to have the ifs to compute if it should be updated, max does it for us. 

            if heights[left] >= heights[right]: #arbitrarily chose >= for left greater than right because if they're the same it doesnt matter which one moves in
                right -= 1
            else:
                left += 1
        return high #no need to move them both in, the computation would be reused