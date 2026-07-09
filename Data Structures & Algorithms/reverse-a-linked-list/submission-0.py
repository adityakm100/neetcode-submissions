# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head #setting default values for previous and current
        
        while curr: #while current exists
            temp = curr.next #set a temp node to store the next node while you modify the CURRENT next
            curr.next = prev #adjust the current's next to be the previous
            prev = curr #set previous to the current, since it would be considered new prev in new iteration
            curr = temp #set the current to the next one that you had stored
        return prev #return prev since prev is what's set to curr every time, so thats the new head