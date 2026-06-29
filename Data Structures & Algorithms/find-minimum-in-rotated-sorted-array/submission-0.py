class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 #starting from the left
        right = len(nums) - 1 #starting from the right

        while left < right: #checking while we haven't checked all the values
            mid = (left + right) // 2 #computing the mid value with this version of left and right
            if nums[mid] > nums[right]: #there is still a sorted nature to the array, just with a break
                left = mid + 1 #move left to mid + 1, halving the search space
            else:
                right = mid #the answer could be at the midpoint since we made it > in the previous condition
        return nums[left] #could return either left or right since they point to the same index
