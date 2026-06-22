class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": #base case to handle empty strings
            return ""
        countT = {} #freq of chars in string t, used as our baseline for which we compare all possible windows to
        window = {} #freq map of chars found in the window between our left and right pointers, we will compare this to the countT dictionary
        res = [-1, -1] #[left, right] pointers of the substring that satisfies our condition
        l = 0
        resLen = float("inf") #new notation for how to set infinity in float

        for c in t:
            countT[c] = 1 + countT.get(c, 0) #remember this is how we handle empty cases not existing specifically in PYTHON HASH  MAP

        matches = 0 #this is the variable we will use to count the number of chars who fulfill the condition that the frequency of the chars in the window is greater than or equal to the frequency of the chars in countT
        need = len(countT) #the number of chars we need to match in order to consider a potential window valid, this is also what we'll compare to to know the instant a window is not valid
        for r in range(len(s)):
            char = s[r] #way to get the char temporarily so we don't keep doing s[r] and make the code look dirty, not really necessary but its nice to have
            window[char] = 1 + window.get(char, 0) #same technique as earlier in order to handle empty cases, more specifically, the get function handles that edge case by having a default value that it can call on, which is the second parameter and in this case we set to 0

            if char in countT and window[char] == countT[char]: #this condition has two parts, one: we dont care about the chars not in the countT frequency map because those are irrelevant chars so if it isn't in the countT map then we ignore it, also since we want to keep track of our matches we check to see if the addition of this very char matches the likelihood of that char in countT, greater than is handled because we don't want to keep updating if its greater than or equal to, just equal to
                matches += 1
            
            while matches == need: #has to be a loop because we want to keep popping chars off while the window is valid
                #potential update of result
                if (r - l + 1) < resLen: #this is really common notation you need to keep in mind, r - l + 1 gives you the size of the window, makes sense because its [l, r), r is not included, so we need to add 1 to include r, checking to see if the potential result we have now is less than the resLen
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1 #pop the leftmost char off
                if s[l] in countT and window[s[l]] < countT[s[l]]: #checking to see if that pop did anything for our matches variable
                    matches -= 1
                l += 1 #move the leftmost pointer in
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""