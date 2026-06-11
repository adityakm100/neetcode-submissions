class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        if not s:
            return 0
        l = 0
        r = 1
        count = 1
        maxCount = 1

        while r < len(s):
            if s[r] not in s[l:r]:
                count += 1
                maxCount = max(maxCount, count)
            else:
                count = 1
                l += 1
                r = l
            r += 1
        return maxCount

        #NOT THE MOST OPTIMAL SOLUTION BECAUSE DOING A SUBSTRING TAKES O(K) TIME WHERE O(K) IS THE SIZE OF THE SUBSTRING
        #PLUS, I'M RESETTING THE RIGHT POINTER BACKWARDS, WHICH MEANS IT CAN TAKE O(N^2) AT WORST TIME
        