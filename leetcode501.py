# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        dic={}
        List=[]
        self.midSearch(root,dic)
        Max=max(dic.values())
        for key,value in dic.items():
            if value==Max:
                List.append(key)
        return List
    
    def midSearch(self,root,dic):
        if not root:
            return 
        self.midSearch(root.left,dic)
        if dic.get(root.val)==None:
            dic[root.val]=1
        else:
            dic[root.val]=1+dic[root.val]
        self.midSearch(root.right,dic)