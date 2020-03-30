# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        sum=0
        L=[]
        head=root
        while root!=None:
            root=root.next
            sum+=1
        if k>sum:
            pre=head
            for i in range(k):
                if i<sum:
                    cur=pre.next
                    pre.next=None
                    L.append(pre)
                    pre=cur
                else:
                    L.append(None)
        else:
            a=sum//k
            b=sum%k
            pre=head
            for i in range(k-1):
                pre2=pre
                if i<b:
                    sum=0
                    while sum<a:
                        pre= pre.next
                        sum+=1
                    cur=pre.next
                    pre.next=None
                    pre=cur
                else:
                    sum=0
                    while sum<a-1:
                        pre= pre.next
                        sum+=1
                    cur=pre.next
                    pre.next=None
                    pre=cur
                L.append(pre2)
            L.append(pre)
        return L