class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        retur = 0 #keeps track of max window size that has the same char

        count = {} #hashmap
        maxf = 0
        
        for r in range(len(s)): #needs the fancy notation with iteration through the string rather than a naive approach of keeping track of r outside and moving through
            count[s[r]] = 1 + count.get(s[r], 0) #hashmap: key: character, value: frequency of that char in string
            maxf = max(maxf, count[s[r]]) #updating the maxf here

            while (r - l + 1) - maxf > k: #contrapositive of the statement we wanted to find, where we want the most frequent char in the window to be within k of the window size so we can replace all the other chars to match the most frequent one
                count[s[l]] -= 1 #we want to remove the existence of that char from both the map and the window
                l += 1
            retur = max(retur, r - l + 1) #update with this particular iteration of window size
        
        return retur