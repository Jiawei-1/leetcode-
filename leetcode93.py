class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        def DFS(s, mix):
            if not s:
                return
            if len(mix) == 3 and int(s) > 255 or len(mix) > 3:
                return
            if len(s) <= 3 and len(mix) ==3 and int(s) <=255 and s[0] != '0' or len(mix) == 3 and s == '0':
                ans.append(mix)
            else:
                for i in range(1,4):
                    if s[0] == '0' and i != 1:
                        break
                    if int(s[0: i]) <= 255:
                        l = mix[0:len(mix)+1]
                        l.append(i)
                        DFS(s[i:], l)  
        DFS(s, [])
        for i in range(len(ans)):
            ans[i] = s[0: ans[i][0]] + '.' + s[ans[i][0]: ans[i][0]+ans[i][1]] + '.' + s[ans[i][0] + ans[i][1] : sum(ans[i])] + '.' + s[sum(ans[i]):]
        return ans
# print(Solution().restoreIpAddresses('00000'))