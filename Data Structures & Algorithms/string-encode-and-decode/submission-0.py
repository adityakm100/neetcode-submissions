class Solution:

    def encode(self, strs: List[str]) -> str:
        stri = ""
        for s in strs:
            stri = stri + str(len(s)) + '#' + s #length of string with delimiter followed by string for easy reading
        return stri

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0 #pointer to keep track of str position
        while i < len(s):
            j = i #keep this as a copy so we don't mess with i and the moving through the loop, THIS IS WHAT I MESSED UP ON
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) #converted integer of a substring from i to j, THIS IS PYTHON NOTATION
            out.append(s[j + 1 : j + 1 + length]) #same notation as above, need to use this for string slicing and substring, start from + 1 because j is at the position of the #
            i = j + 1 + length #places the pointer of string position at the character we just appended, makes sense because j + 1 + length is not included in the slice.
        return out

        
