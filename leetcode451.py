import collections
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return ''.join(k*v for k,v in collections.Counter(s).most_common())
        dic={}
        res=[]
        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        l=sorted(dic.items(),key=lambda item: item[1], reverse= True)
        for i in l:
            res.append(i[0]*i[1])
        return ''.join(res)
