class MinStack:

    curr_min = math.pow(2, 31)

    def __init__(self):
        self.stack = [] #actual stack of values
        self.minStack = [] #stack holding the minimum value at the time, just cached at the end
    def push(self, val: int) -> None:
        self.stack.append(val) #always add to new stack
        if len(self.minStack) == 0: #if first val, add to minStack as well
            self.minStack.append(val)
        else:
            curr_min = min(val, self.minStack[-1]) #find the min between the latest value and the curr and add that in, duplicates don't really matter, O(n) space to play with
            self.minStack.append(curr_min) #add this min value

    def pop(self) -> None:
        self.stack.pop() #pop from stack
        self.minStack.pop() #pop 

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
