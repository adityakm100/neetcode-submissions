class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count = [0] * 26
        count1 = [0] * 26
        
        for i in range(len(s1)):
            count[ord(s1[i]) - ord('a')] += 1
            count1[ord(s2[i]) - ord('a')] += 1
        
        if count == count1:
            return True
        
        for r in range(len(s1), len(s2)):
            count1[ord(s2[r]) - ord('a')] += 1
            count1[ord(s2[r - len(s1)]) - ord('a')] -= 1

            if count == count1:
                return True
        return False
