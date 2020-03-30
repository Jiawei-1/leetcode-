# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self,head):
        if not head or not head.next:
            return head
        else:
            head2=head
            pre=head2
            cur1=pre.next
            cur2=cur1.next
            pre.next=None
            while cur2!=None:
                cur1.next=pre
                pre=cur1
                cur1=cur2
                cur2=cur2.next
            cur1.next=pre
            return cur1

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head ==None or head.next==None:
            return True
        h=head
        sum=0
        while h!=None:
            h=h.next
            sum+=1
        if sum%2 ==0:
            s=sum/2
        else:
            s=sum/2+1
        h=head
        while s!=0:
            h=h.next
            s-=1
        h=self.reverse(h)
        while h!=None:
            if h.val!=head.val:
                return False
            else:
                h=h.next
                head=head.next
        return True



