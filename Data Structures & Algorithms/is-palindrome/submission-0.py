class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        alphanumeric = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        for char in s:
            if char == " " or char not in alphanumeric:
                continue
            string += char.lower()
        print(string)
        left = 0
        right = len(string) - 1

        while (left < right):
            if (string[left] != string[right]):
                return False
            left += 1
            right -= 1
        return True
        