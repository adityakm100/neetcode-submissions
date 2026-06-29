class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        while left <= right: #binary search condition for loop
            mid = (left + right) // 2 #middle assuming the previous left and right
            hours = 0 #number of hours taken with this particular iteration of mid being the eating speed
            for p in piles:
                hours += math.ceil(p / mid) #adding a rounded up version of how many hours needed to consume each individual pile with this version of mid
            
            if hours <= h: #if the number of hours is within the target
                right = mid - 1 #try to find an even smaller version of bananas per hour that satisfy the target, moving binary search in
                res = mid #set the result to the current iteration of mid we have
            else:
                left = mid + 1 #our current mid is too restrictive, find a higher bananas per hour speed on the right side of the search space between [1, max(piles)]
        return res

#ALGORITHM: This algorithm is a natural extension of the brute force algorithm where we would check every number between 1 and the maximum number of bananas in the pile to find which is the smallest value that can be set as bananas per hour
#However, instead of brute forcing that set [1, max(piles)], we use binary search to arrive at a solution more efficiently, nlogm time instead of nm time
