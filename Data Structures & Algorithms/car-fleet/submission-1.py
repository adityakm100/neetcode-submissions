class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #OFFICIAL PYTHONIC SOLUTION
        pair = [[p, s] for p,s in zip(position, speed)] #called list comprehension, basically doing the iterating through for loop of the zipped position and speed arrays and then storing that pair, so its a array of pairs
        stack = [] #monotonic stack designed to keep all the individual fleets that will reach on time, if anything is less than the top element in the stack, then its guaranteed to come earlier and join up with one of the cars, even if it isn't the top one

        for p, s in sorted(pair)[::-1]: #Sorting in reverse through the sorted list of pairs
            time = float((target - p) / s) #store the current time
            if stack and time <= stack[-1]: #if the stack exists and the time computed is less than the time on top, just continue, we only want to store the monotonically increasing order of cars, these are the fleets
                continue
            stack.append(time) #append it if its greater than the top element
        return len(stack) #number of unique car fleets that can arrive