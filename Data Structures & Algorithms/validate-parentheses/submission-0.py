class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #the way to represent a stack in python is just to use a python list
        closeToOpen = {"}": "{", ")": "(", "]": "["} #hashmap with key of closing parentheses and value of the corresponding opening parentheses, this is also a way of initializing a hashmap with the keys and values we want it to store {key: value, key2: value2}

        for c in s:
            if c in closeToOpen: #if the character is a closing parenthesis character, we want to check if the corresponding opening character is in the stack
                if stack and stack[-1] == closeToOpen[c]: #if the stack is empty at any point not at the end, then its not valid, stack[-1] is how to get the latest character added, compare most recent character to the opening parentheses corresponding to the closing one, make sure they're the same
                    stack.pop() #if condition match, pop out the opening parentheses
                else:
                    return False
            else:
                stack.append(c) #we can add as many opening or non closing parentheses as we want
        
        return True if not stack else False #if the stack is empty at the end, its valid, if there's any characters left, its not valid