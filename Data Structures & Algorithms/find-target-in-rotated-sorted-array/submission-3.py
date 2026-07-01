class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 #starting at 0
        right = len(nums) - 1 #starting at the end

        while left <= right: #checking to make sure our binary search condition is still valid
            mid = (left + right) // 2 #compute this iteration of mid, remember to use // for integer division
            if nums[mid] == target: 
                return mid #will always hit as long as element exists since you will always search through the sorted element that matters due to the if and ELSE nature
            if nums[left] <= nums[mid]: #if the left side of the array continues to be sorted, we want to check through the rest of these elts, this condition has to be <= since on a 2 elt array, left and mid could be the same thing and it still is sorted if its 2 one element sorted arrays
                if nums[left] <= target < nums[mid]: #checking to see if the target is greater than or equal to the leftmost elt in the array while still being in the left side, thats why there is an in-between portion
                    right = mid - 1 #this means that it is both in the sorted array portion and in the leftmost side of the sorted array, so search through this leftmost sorted array by moving the RIGHT pointer in 
                else:
                    left = mid + 1 #since the right side is also sorted, but in a different sorted order, we would check through those too. 
            else: #the right side of the array must be the sorted side we're looking for then
                if nums[mid] < target <= nums[right]: #checking to see if matches the criteria of the right side of the sorted array
                    left = mid + 1 #if so, explore that RIGHT side by moving the left pointer in
                else:
                    right = mid - 1 #it has to be in the other sorted element if not in this one, so check that one too

        return -1 #if not found, then and only then will this condition hit

    #THIS ALGORITHM IS PREDICATED ON THE PART THAT THERE IS A DISCONNECT BETWEEN TWO SORTED ELEMENTS, AND YOU NEED TO CHECK THROUGH EACH SORTED ELEMENT INDIVIDUALLY BASED ON HOW ITS SORTED.
