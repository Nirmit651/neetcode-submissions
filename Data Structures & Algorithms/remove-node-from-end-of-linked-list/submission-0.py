# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        size = 0
        current = head
        while current:
            size += 1
            current = current.next

        prev = None
        current = head
        #get node to remove
        for i in range(size-n):
            prev = current
            current = current.next

        if prev is None:
            return head.next
        
        prev.next = current.next
    
        return head

        