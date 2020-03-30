class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        s=set()
        for edge in edges:
            s.add(edge[0])
            s.add(edge[1])
        flags=disjoint(len(s)+1)
        for edge in edges:
            x=flags.find(edge[0])
            y=flags.find(edge[1])
            if x!=y or (flags.array[x]==-1 and flags.array[y]==-1):
                flags.union(edge[0],edge[1])
            else:
                ans=edge
        return ans
class disjoint(object):
    def __init__(self,i):
        self.array=[-1]*i

    def union(self,i,j):
        i=self.find(i)
        j=self.find(i)
        if i!=j or (self.array[i]==-1 and self.array[j]==-1):
            self.array[i]=j

    def find(self,i):
        while self.array[i]!=-1:
            i=self.array[i]
        return i
