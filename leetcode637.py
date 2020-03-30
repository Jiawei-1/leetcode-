# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
#     def averageOfLevels(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[float]
#         """
#         if not root:
#             return []
#         list1=[]
#         list2=[]
#         list3=[]
#         list1.append(root)
#         while list1:
#             Sum=0
#             s=len(list1)
#             for i in range(s):
#                 Sum+=list1[i].val
#                 if list1[i].left:
#                     list2.append(list1[i].left)
#                 if list1[i].right:
#                     list2.append(list1[i].right)
#                 # list1.pop(0)
#             list3.append(float(Sum) / float(s))
#             list1=list2
#             list2=[]
#         return list3
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        s=[]
        c=[]
        def deepsearch(root,i,s,c):
            if not root:
                return s,c
            if len(s)==i:
                s.append(0)
                c.append(0)
            s[i]+=root.val
            c[i]+=1
            i+=1
            s,c=deepsearch(root.left,i,s,c)
            s,c=deepsearch(root.right,i,s,c)
            return s,c
        s,c=deepsearch(root,0,s,c)
        for i in range(len(s)):
            s[i]=float(s[i])/float(c[i])
        return s
            