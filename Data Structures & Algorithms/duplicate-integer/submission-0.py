class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDupe = set(nums)
        if len(noDupe) != len(nums):
            return True
        return False