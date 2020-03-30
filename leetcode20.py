class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[]
        mapping={'}':'{',']':'[',')':'('}
        for i in s:
            if i in mapping:
                first= l.pop() if len(l)!=0 else '?'
                if first != mapping[i]:
                    return False
            else:
                l.append(i)
        if len(l)==0:
            return True
        else:
            return False
        # l=[]
        # for i in s:
        #     if i in ['(','{','[']:
        #         l.append(i)
        #     elif i==')':
        #         if len(l)==0:
        #             return False
        #         if l[-1]=='(':
        #             l.pop()
        #         else:
        #             return False
        #     elif i=='}':
        #         if len(l)==0:
        #             return False
        #         if l[-1]=='{':
        #             l.pop()
        #         else:
        #             return False
        #     elif i==']':
        #         if len(l)==0:
        #             return False
        #         if l[-1]=='[':
        #             l.pop()
        #         else:
        #             return False
        # if len(l)==0:
        #     return True
        # else:
        #     return False             

