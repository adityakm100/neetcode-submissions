class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictio = defaultdict(list) #mapping charCount to list of Anagrams
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1 #80 - 80 = 0 for a, 81 - 80 = 1 for b, etcetera
            dictio[tuple(count)].append(word) #only making it tuple because python cant have lists as keys
        return list(dictio.values()) #needs to be wrapped in list because of what .values() returns (A view object)
