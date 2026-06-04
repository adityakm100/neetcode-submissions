class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort() #best way to sort in-place, sorted(nums) would create a whole new sorted array

        for i in range(len(nums)): #first loop to check per elt
            if i > 0 and nums[i] == nums[i-1]: #all duplicates will be to the left of the current in a sorted array, since in [-1, -1, 2], first one is fine, second is duplicate since -1 is on right, and third is fine since 2 is different from -1
                continue
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[j] + nums[k] + nums[i] #make sure to include the outside loop value as well, that was my mistake
                if total > 0:
                    k -= 1
                elif total < 0: 
                    j += 1
                else:
                    out.append([nums[i], nums[j], nums[k]])
                    j += 1 #note on this code, the reason we only update the left pointer and not the right is because there is only one sum that works if we just shift the left pointer, so no matter what, based on the way this code is written with the two earlier conditions coming in and knocking off a bunch of the cases, we can just increment the left. The old way I had of writing the code needed the old way of checking, with both left and right incremented and checked, because I checked == 0 first. ALWAYS START WITH THE MORE BROAD CASES FIRST and check the too big and too small cases first
                    while nums[j] == nums[j - 1] and j < k: #duplicate check + making sure we're in bounds check
                        j += 1 #still had to be updated once outside the loop but we keep updating it inside the loop
        return out