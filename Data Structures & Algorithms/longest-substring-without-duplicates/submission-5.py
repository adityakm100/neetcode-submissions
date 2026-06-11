class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        charSet = set() #Initialization of a set in Python, just for more reminders, also set is used to keep track of all chars in string/substrings
        l = 0
        maxCount = 0
        
        for r in range(len(s)): #fancy notation, instead of initializing a right pointer, just use it in loop and have the same behavior, this version acts like a for(int i = ...) loop in C++ anyways, going through each individual index
            while s[r] in charSet: #we want to check existence of chars in charset first because this is the limiting factor determining the size of the window
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r]) #in total, the charset is just keeping track of all the unique chars, moving the window in if that window has a duplicate char
            maxCount = max(maxCount, r - l + 1) #we need to add one because an individual character by itself is considered a longest substring of 1, not 0
        return maxCount

        