class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums) #store 1 because 0 will negate the value of the prefix, for example [1,2,3,4], 1 *0 = 0, we want 1 for the prefix of 1
        pre = 1 #same logic as above
        post = 1
        for i in range(len(nums)): #left pass through the array
            output[i] = pre #store the value in output since no extra space, we want to keep the prefixes to the right since when computing product besides self, we want the product of the prefix of the left ([1,2,3,4] sans 3 we want product of prefix of 2 (1*2) * product of postfix of 4 (4))
            pre *= nums[i] #increment prefix by the sum of the current val
        for mum in range(len(nums) - 1, -1, -1): #again, logic for iterating in reverse (right pass through the array)
            output[mum] *= post #we want to multiply the output slot to the left (handled by nature of array indexing always being one less than expected) by the postfix (since as example mentioned, we want to multiply by product of postfix to the right)
            post *= nums[mum] #increment postfix by the sum of the val since we're going backwards, logic should be the same
        return output