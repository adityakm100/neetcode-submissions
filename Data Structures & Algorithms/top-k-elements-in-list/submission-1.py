class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictio = {} #maps each integer to its number of occurrences
        freq = [[] for i in range(len(nums) + 1)] #needs to be plus one because there could be 0 occurrences

        for n in nums:
            dictio[n] = 1 + dictio.get(n,0) #failsafe again
        for n,c in dictio.items(): #int, freq in count.items()
            freq[c].append(n) #basically flipping the order, for every number of occurrents [1,1,1,2,2] for every elt that occurs 3 times, add 1 to it
        res = []
        for i in range(len(freq) - 1, 0, -1): #special range based for loop logic, (start, end, inc/dec)
            for n in freq[i]: #since the number of times an elt occurs in an array isn't always 1 [1,1,2,2], where 1 and 2 occurs twice, they would both be listed under 2 in the freq table
                res.append(n) #won't ever go over since we go elt by elt basis
                if len(res) == k:
                    return res