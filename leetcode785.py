class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        if not graph:
            return True
        color={}
        for i in xrange(len(graph)):
            if color.get(i)==None:
                Node=graph[i]
                stack=[i]
                color[i]=1
                while stack:
                    cur=stack.pop()
                    Node=graph[cur]
                    for j in Node:
                        if j not in color:
                            stack.append(j)
                            color[j]=color[cur]*-1
                        elif color[cur]==color[j]:
                            return False
        return True