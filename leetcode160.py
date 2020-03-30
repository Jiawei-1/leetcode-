# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
           
class Solution(object):

    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 当A遍历完后指向B，B遍历完后指向A 
        # A+B长度是一样的
        # 如果有相同的节点，第一遍就能找到
    
        if headA ==None or headB==None：
            return None
        curA=headA 
        curB=headB
        while curA != curB：
            curA=curA.next if curA!=None else headB
            curB=curB.next if curB!=None else headA
        return curA