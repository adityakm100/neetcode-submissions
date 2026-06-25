class Solution:

    #ALGORITHM: have two arrays, an output initialized to 0s same length as temperature, and a stack that is monotonically decreasing. Add the first element in and compare between elements while iterating. If element is greater than top of stack, keep popping while the top is less than the element being added, preserve monotonic decreasing so we can compute how far it is from each elt for the outout array

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures) #same length as input array, stores the number of days until a warmer temperature for each i'th day
        stack = [] #monotonically decreasing stack by nature, add a pair [temp, index]

        for i in range(len(temperatures)): #iterate through the temps
            while stack and temperatures[i] > stack[-1][0]: #while loop might not iterate, so its not O(n^2), check to see if the stack exists because if its empty it has to be added and it has to keep being popped while the current elt is greater than the top
                index = stack.pop()[1] #could also be written as temp, index = stack.pop(), my way only gets the index since the temperature is useless to us
                out[index] = i - index #update that indices position in the out array since they are the same size and it refers to that space in the input array with the difference in indices between the current greater temp and that temp
            stack.append([temperatures[i], i]) #append the pair of temperatures and index for this position
        return out #return
