# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l1 = head
        l2 = slow.next
        slow.next = None 

        prev = None
        while l2:
            next_node = l2.next
            l2.next = prev
            prev = l2
            l2 = next_node

        l2 = prev
        
        while l2:
            next1, next2 = l1.next, l2.next
            l1.next = l2
            l2.next = next1

            l1 = next1
            l2 = next2        