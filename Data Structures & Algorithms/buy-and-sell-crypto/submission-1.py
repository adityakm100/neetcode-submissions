class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1 #not at the end inwards, we want to check the nearest possible combination closest to left and expand r outwards while its still working, so initialization of right is one more than left
        maxProfit = 0

        while r < len(prices): #left pointer shouldn't matter because left pointer only gets updated towards the right pointer on the failed iteration, right pointer is the one that keeps moving outwards so that is the only condition being checked, left pointer just gets moved to a position that right pointer has always checked
            if prices[l] < prices[r]: #only calculate profit if there is a clear profit since we can always return 0 if there is no good profitable transaction
                p = prices[r] - prices[l] #temp profit value
                maxProfit = max(maxProfit, p) #update max profit
            else:
                l = r #we want the left pointer to be at the absolute minimum that it can possibly be, so through our algorithm, left will always inherently be placed at a local minimum. If the global minimum is at the end, there is no effect on calculations since there are computations done with a local minimum, but we wouldn't just increment it by 1
            r += 1 #we always iterate right no matter what since if we update left to be at right, right would be one to the right which is what we want, otherwise, if the price of right was still higher meaning better sell, we iterate right to try to find a new potential better sell
        return maxProfit

        #WITH SLIDING WINDOW, IT SEEMS LIKE YOU NEVER MOVE A POINTER BACK LIKE YOU DO IN MY PREVIOUS THINKING, if a particular combination of {l,r} fails, then l gets moved TO R, not just incremented by 1, and r gets moved forward, NEVER MOVED BACK, that would make it O(n^2) i think