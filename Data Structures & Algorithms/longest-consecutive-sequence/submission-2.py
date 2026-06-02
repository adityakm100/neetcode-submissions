class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dictio = set(nums) #use a set since we only want to check existence of a number, no hashmap needed
        maxCounter = 0 #return counter
        counter = 0 #temp counter per subsequence
        
        for key in dictio:
            if (key - 1) not in dictio: #checks to make sure this is start of sequence, no redundant counting
                counter = 1
                while (key + counter) in dictio: #still linear, since max size is the length of the input list
                    counter += 1
                maxCounter = max(maxCounter, counter)
        
        return maxCounter