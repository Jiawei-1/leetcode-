# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def length(self,head):
        sum=0
        while head!=None:
            sum+=1
            head=head.next
        return sum
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next==None or head.next.next==None:
            return head
        pre=head
        cur=head.next
        cur.next=self.oddEvenList(cur.next)
        l=self.length(cur.next)
        a=l%2
        if a==0:
            l=l//2
        else:
            l=l//2+1
        pre.next=cur.next
        h=cur
        while l>0:
            l-=1
            h=h.next
        cur.next=h.next
        h.next=cur
        return head
        
