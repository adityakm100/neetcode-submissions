class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights) #length of the array 
        stack = [] #monotonic stack
        maxArea = 0

        for i in range(n): #iterating through elements
            start = i #we set a start element to the current position because if an element is smaller than the one before it, then it can be "extended" to the left to make a potential area that includes the element that is also being popped. When it is saved to the previous element in the loop, this is the code way of saying that if we were to use this element as a height, you could also extend it all the way back to the last popped element
            while stack and heights[i] < stack[-1][0]: #checking to see if stack exists and if the current height is LESS definitively than the top element on the stack
                height, index = stack.pop() #pop the element
                width = i - index #width is current index minus the stored index, which remember can be extended outwards, so its the index of the earliest element that you can make a rectangle out of
                maxArea = max(maxArea, height * width) #height is stored in the stack, so simple calculation to update max
                start = index #important part, again if the element is smaller than the previous, then at the very least, you can make a rectangle of the smaller height that includes this now popped element because you can extend it leftwards
            stack.append([heights[i], start]) #append either with the current i index or with the modified (accounting for heights of previous elts) start position
        
        for h, i in stack: #EDGE CASE, at the end of the runthrough, there still may be elts in the stack that you want to consider their height
            maxArea = max(maxArea, h*(n - i)) #you're at the end, so use the length as the subtractor instead of any elt index i
        return maxArea

        #NOT THE MOST OPTIMAL SOLUTION, BUT IT WORKS, IF WE DONT WANT TO CHECK THE EDGE CASE, WE CAN SETUP A SHADOW ELEMENT AT N+1 WITH LENGTH 0, ITERATRE THROUGH THAT RANGE AND CONSIDER IN THE LOOP WHETHER I IS AT N AND ALSO CHECK THE WIDTH BEING AT I IF THE STACK DOESNT EXIST SINCE YOU ARE CHECKING A PHANTOM ELEMENT
