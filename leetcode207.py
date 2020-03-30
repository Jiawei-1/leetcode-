class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        flags=[0]*numCourses
        List=[[]for _ in range(numCourses)]
        for i,j in prerequisites:
            List[i].append(j)

        def dfs(i, List, flags):
            if flags[i]==-1:
                return True
            if flags[i]==1:
                return False
            if not List[i]:
                flags[i]=-1 
                return True
            flags[i]=1
            for j in List[i]:
                if not dfs(j,List,flags):
                    return False
            flags[i]=-1
            return True
        
        for i in range(numCourses):
            if not dfs(i,List,flags):
                return False
        return True
# print(Solution().canFinish(7,[[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]))