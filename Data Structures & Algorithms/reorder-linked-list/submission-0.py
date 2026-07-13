# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1, 2, 3, 4, 5
# 1, 2, 3, 5, 4
# 1, 5, 2, 4, 3

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: #if the list doesn't exist or has two values, no point in returning anything
            return None

        slow, fast = head, head #tortoise and hare pointers

        while fast and fast.next: #condition to check for hare not breaking the list
            slow = slow.next
            fast = fast.next.next

        #USED TO FIND THE MIDDLE OF THE LIST, THIS HELPS US FIND WHERE TO START REVERSING
        prev, curr = None, slow.next #start reversing the list from the node right after the middle
        slow.next = None #sever that list, we don't want it to impact our current list
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp #classic list reversal
        
        #REVERSE THE SECOND HALF OF THE LIST
        first, second = head, prev #create pointers to head and prev, which is the start of the true list and the start of the reversed list specifically

        while second: #second will always be shorter or same, either on even lists, where they're the same size or odd lists, where they're guaranteed shorter, so if we base it on second, first will always have nodes to populate with too
            tmp1 = first.next #store values of the next values similar to reversing list so you don't reverse to a None pointer while changing anything
            tmp2 = second.next

            first.next = second #first's next value should be first value in reversed list, or second
            second.next = tmp1 #next value of the list should be the value after the first value in the normal list, almost like a zipper

            # two lists now: first: 1 -> 2 -> 3 -> None
            #second: 5 -> 4 -> None

            #first.next = second, means 1 connects to 5: 1 -> 5
            #second.next = tmp1, means 5 connects to 2, 5 is already connected to 1: 1 -> 5 -> 2
            #first being set to next value and so is second sets up new prongs of zipper

            first = tmp1 #first should be moved up one
            second = tmp2 #so should second


        
        