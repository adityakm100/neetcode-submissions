class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictio = defaultdict(int)
        lis = []
        i = 0
        for num in nums:
            dictio[num]+=1
        while (i < k):
            v = max(list(dictio.values()))
            index = list(dictio.values()).index(v)
            lis.append(list(dictio.keys())[index])
            del dictio[list(dictio.keys())[index]]
            i+=1
        return lis
