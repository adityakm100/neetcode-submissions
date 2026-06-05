class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        high = 0

        while (left < right):
            curMax = min(heights[left], heights[right]) * (right - left)
            high = max(high, curMax)

            if heights[left] >= heights[right] :
                right -= 1
            else:
                left += 1
        return high