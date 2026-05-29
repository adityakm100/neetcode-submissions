class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        index = 0
        for num in nums:
            diff = target - num
            for key in hashmap:
                if key == diff:
                    val1 = index
                    val2 = hashmap[key]
                    if (val1 > val2):
                        return [val2, val1]
                    return [val1, val2]
            hashmap[num] = index
            index+=1