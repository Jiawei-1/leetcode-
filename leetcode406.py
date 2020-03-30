class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda a:(-a[0],a[1]))
        ans=[]
        for p in people:
            ans.insert(p[1],p)
        return ans