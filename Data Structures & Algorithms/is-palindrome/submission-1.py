class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum(): #keep going through the characters and skip if its not a num, REMEMBER isalnum()
                l += 1
            while r > l and not s[r].isalnum(): #have to include the check again (r>l or l < r) because l and r are actively updated and might accidentally influence the results if we don't check early and break out
                r -=1
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True