# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) #way of initializing a list node with backup value of 0 to prevent any edge cases, need this cause you could remove the actual head
        
        slow = fast = dummy #set the slow and fast pointers to this dummy node
        for _ in range(n):
            fast = fast.next #move fast n nodes ahead of slow
        
        while fast.next: #keep going while fast has nodes to go to
            slow = slow.next
            fast = fast.next

        #at the end of this loop, slow would be on the n'th node from the end, since fast started n nodes ahead, slow would be at total - n, which is where it should be
        
        slow.next = slow.next.next #way of popping the node off the linked list by setting its next node to be the one after it
        return dummy.next #start of the linked list since the dummy node was initialized to the head or 0, where next would be None as expected