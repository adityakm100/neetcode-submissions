# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode() #setting up a dummy node to start the list to avoid edge cases, common practice

        while list1 and list2: #checking to see while the two lists have values associated with them
            if list1.val < list2.val: #if list1's val is minimum, add it to the end of the dummy list, update list1 pointer
                tail.next = list1
                list1 = list1.next
            else: #this is if list2 is same or less
                tail.next = list2
                list2 = list2.next
            tail = tail.next #we need to update the dummy pointer to point to the next one, otherwise they'll all add after the dummy exactly instead of extending outwards
        tail.next = list1 or list2 #adding the remaining nodes to the end based on if they exist

        return dummy.next #stores the original dummy starting, so dummy.next is equal to the first starting node
        