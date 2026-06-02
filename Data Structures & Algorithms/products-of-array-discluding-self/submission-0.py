class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        pre = 1
        post = 1
        output[0] = pre
        for i in range(len(nums)):
            output[i] = pre
            pre *= nums[i]
        for mum in range(len(nums) - 1, -1, -1):
            output[mum] *= post
            post *= nums[mum]
        return output