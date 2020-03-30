# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        num=0
        cur=head
        while cur!= None:
            cur= cur.next
            num+=1
        if num<n:
            return head
        elif num==1 and n==1
            return None
        else:
            cur=head
            x=num-n
            y=1
            while y<x:
                cur=cur.next
                y+=1
            if n==1:
                cur.next=None
            elif n==num:
                head=head.next
            else:
                cur.next=cur.next.next 
        return head
