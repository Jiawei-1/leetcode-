class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r*c!=len(nums)*len(nums[0]):
            return nums
        
        l=[]
        sub=[]
        s=0
        for i in range(r):
            for j in range(c):
                
                a=s//len(nums[0])
                b=s%len(nums[0])
                sub.append(nums[a][b])
                s+=1
            l.append(sub)
            sub=[]
        return l