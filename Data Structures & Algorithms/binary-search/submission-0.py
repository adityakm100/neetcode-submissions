class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start)//2 
            potential = nums[mid]
            if potential == target:
                return mid
            elif potential > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
            