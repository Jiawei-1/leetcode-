# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        pre=self.midReturn(head)
        mid=pre.next
        pre.next=None
        root=TreeNode(mid.val)
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(mid.next)
        return root
    
    def midReturn(self,head):
        if not head:
            return 
        slow=head
        fast=head.next
        pre=head
        while fast!=None and fast.next!=None:
            pre=slow
            slow=slow.next
            fast=fast.next.next
        return pre