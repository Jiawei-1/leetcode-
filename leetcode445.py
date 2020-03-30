# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1=0
        num2=0
        now=None
        while l1:
            num1=num1*10+l1.val
            l1=l1.next
        while l2:
            num2=num2*10+l2.val
            l2=l2.next
        sum=num1+num2
        if sum==0:
            return ListNode(0)
        while sum!=0:
            cur =ListNode(sum%10)
            cur.next= now
            now=cur
            sum=sum//10
        return now