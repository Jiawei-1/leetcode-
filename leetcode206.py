# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head = None or head.next==None:
            return head
        p = head
        c= head.next
        p.next=None
        while c.next!= None:
            c2= c.next
            c.next=p
            p=c
            c=c2
        c.next=p
        return c