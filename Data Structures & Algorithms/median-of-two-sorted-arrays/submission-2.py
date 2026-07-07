class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2 #using A and B to make it easier to number
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A): #we want to perform binary search on the smaller array
            A,B = B,A #swapping the elements
        
        l, r = 0, len(A) - 1
        while True: #always going to be a median, want to return when done, this just ensures that it will continue to loop
            i = (l + r) // 2 #this is the mid of A
            j = half - i - 2 #subtract 2 for the index offset since i and j start at 0 and we want them to start at 1, this would also be the mid of B

            Aleft = A[i] if i >= 0 else float("-inf") #technically any of these indices can be out of bounds, so this would set a default value to it and have it be -infinity if it is out of bounds
            Aright = A[i + 1] if i + 1 < len(A) else float("inf") #however, if the right pointer is out of bounds, that means it is greater than the length, so we would want everything, therefore we would set to positive infinity
            Bleft = B[j] if j >= 0 else float("-inf") #The key thing to keep in mind here is whether it is the left or right partition
            Bright = B[j + 1] if j + 1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright: #this would enter the condition IF THE LEFT PARTIITON IS CORRECT
                if total % 2: #this is really clever, this would equal 1 if its odd, which is ALSO TRUE in num format
                    return min(Aright, Bright)
                else: #even in this case, since it would equal 0, which would be false before
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            elif Aleft > Bright: #this is if the partition isn't correct specificially because the left side is too big, so you move right in to make the elements smaller
                r = i - 1 #moving the left partition on the smaller element in, which affects the dynamics of how elements are separated on both arrays due to how half the variable interacts with it
            else: #this is if the partition isn't correct specifically if the left side on A is too small, so you move the left side in to get bigger elts
                l = i + 1
            