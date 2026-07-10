# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head #we want both the slow and fast pointers to start at the initial head

        while fast and fast.next: #while both fast and the next pointer of fast exists since fast will reach faster to the end than slow
            slow = slow.next #move slow one iteration
            fast = fast.next.next #move fast two iterations

            if slow == fast: #if slow ever reaches fast, there exists a cycle
                return True #cycle
            
        return False #if fast ever reaches a null, then this will not be a cycle

        #FLOYDS TORTOISE AND HARE ALGORITHM, ALWAYS RUNS IN O(N) TIME SINCE THE MAXIMUM CYCLE POSSIBLE IS AN ENTIRE LIST CYCLE AND SINCE THE DIFF BETWEEN SLOW AND FAST DECREASES BY 1, GUARANTEED TO MEET