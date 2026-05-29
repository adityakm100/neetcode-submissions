class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmaptot = {}
        hashmapone = {}
        conc = s + t
        for char in conc:
            hashmaptot[char] = hashmaptot.get(char, 0) + 1
        for char in s:
            hashmapone[char] = hashmapone.get(char, 0) + 1
        if len(hashmaptot) != len(hashmapone):
            return False
        for i in hashmaptot:
            if hashmaptot[i] % 2 != 0:
                return False
        return True
        
        