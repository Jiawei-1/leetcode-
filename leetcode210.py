class Solution(object):
    def findOrder(self, numCourses, prerequisites):     #DFS
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        def dfs(i,List,flags,ans):
            if flags[i]==1:
                return False
            if flags[i]==-1:
                return True
            flags[i]=1
            for pre in List[i]:
                if not dfs(pre,List,flags,ans):
                    return False
            flags[i]=-1
            ans.append(i)
            return True
        flags=[0]*numCourses
        List=[[] for _ in range(numCourses)]
        for i,j in prerequisites:
            List[i].append(j)
        ans=[]
        for i in range(numCourses):
            if not dfs(i,List,flags,ans):
                return []
        return ans

        # # pre=[[] for _ in range(numCourses)]        拓扑排序
        # end=[[] for _ in range(numCourses)]
        # Nums=[0]*numCourses
        # for i,j in prerequisites:
        #     Nums[i]+=1
        #     end[j].append(i)
        # # for i in range(numCourses):
        # #     Nums[i]=len(pre[i])
        # queue=[]
        # ans=[]
        # for i in range(numCourses):
        #     if Nums[i]==0:
        #         queue.append(i)
        # while queue:
        #     cur=queue.pop(0)
        #     ans.append(cur)

        #     for j in end[cur]:
        #         Nums[j]-=1
        #         if Nums[j]==0:
        #             queue.append(j)
        # if len(ans)==numCourses:
        #     return ans
        # return []
        