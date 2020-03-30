# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        List=self.getList(root)
        i=0
        j=len(List)-1
        while i<j:
            if List[i]+List[j]==k:
                return True
            elif List[i]+List[j]<k:
                i+=1
            else:
                j-=1
        return False

    
    def getList(self, root):
        if not root:
            return []
        stack=[]
        List=[]
        while stack!=[] or root:
            if root:
                stack.append(root)
                while root.left:
                    root=root.left
                    stack.append(root)
            root=stack.pop()
            List.append(root.val)
            root=root.right
        return List