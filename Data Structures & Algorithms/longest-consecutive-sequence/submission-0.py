class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dictio = defaultdict(int)
        maxCounter = 0
        counter = 0
        for num in nums:
            dictio[num] += 1
        for key in dictio:
            if (key - 1) not in dictio:
                counter = 1
                while (key + counter) in dictio:
                    counter += 1
                maxCounter = max(maxCounter, counter)
            else:
                counter = 1
        
        return maxCounter