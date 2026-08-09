# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #if list is empty or length of 1
        if(head==None or head.next==None):
            return head;

        prev = head
        current = head.next
        nextNode = head.next.next

        #list is of size 2
        if(nextNode==None):
            current.next = head
            head.next = None
            head = current
            return head

        #list is greater than size 2
        while(current!=None):
            current.next=prev
            prev = current
            current=nextNode
            if(nextNode == None or nextNode.next==None):
                nextNode=None
            else:
                nextNode=nextNode.next
        head.next=None
        head = prev

        return head
