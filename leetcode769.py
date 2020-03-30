class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        index=0
        Max=0
        for i in range(len(arr)):
            Max=max(arr[i],Max)
            if Max==i:
                index+=1
        return index
# print(Solution().maxChunksToSorted([0,1,3,4,2]))