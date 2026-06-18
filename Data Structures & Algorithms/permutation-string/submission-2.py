class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): #basic check to make sure there even can be a permutation
            return False
        
        count = [0] * 26 #frequency array of the smaller string that needs to be checked
        count1 = [0] * 26 #frequency array of the window through the larger string

        for i in range(len(s1)):
            count[ord(s1[i]) - ord('a')] += 1 #setting the frequency array of the small string
            count1[ord(s2[i]) - ord('a')] += 1 #setting the frequency array of the first window, cant be checked through the big loop
        
        if count == count1: #checking if arrays are equal
            return True
        
        for r in range(len(s1), len(s2)):
            count1[ord(s2[r]) - ord('a')] += 1 #adding the freqeuncy of the right most pointer of the sliding window
            count1[ord(s2[r - len(s1)]) - ord('a')] -= 1 #removing the frequency of the left most pointer of the sliding window, the char that we just passed over

            if count == count1: #checking on every iteration if the new count1 array matches our original count frequency of the smaller string with permutation
                return True
        return False #if it passes through the whole thing, it fails

