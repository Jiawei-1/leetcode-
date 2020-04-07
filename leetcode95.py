# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generateBST(List):
            if not List:
                return [None]
            if len(List)==1:
                return [TreeNode(List[0])] 
            ans=[]  
            for i,j in enumerate(List):
                left=generateBST(List[:i])
                right=(generateBST(List[i+1:]) if i<len(List)-1 else [None])
                for l in left:
                    for r in right:
                        node=TreeNode(j)
                        node.left=l
                        node.right=r
                        ans.append(node)
            return ans
        if n ==0:
            return []
        List=[]
        for i in range(n):
            List.append(i+1)
        return generateBST(List)
# Solution().generateTrees(3)


                