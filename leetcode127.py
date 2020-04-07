class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        head = [beginWord,]
        tail = [endWord,]
        l = len(beginWord)
        tmp = 'qwertyuioplkjhgfdsazxcvbnm'
        ans = 2
        ws=set(wordList)
        while head:
            if len(head) > len(tail):
                tail, head = head, tail
            stack = set()
            for cur in head:
                for i in range(l):
                    for j in tmp:
                        word = cur[:i] + j + cur[i+1]
                        if word in tail:
                            return ans
                        if word in ws:
                            stack.add(word)
                            ws.remove(word)
            head = stack
            ans += 1
        return 0
    #     stack2=[]
    #     ans = 2
    #     while head != []:
    #         if len(head) > len(last):
    #             head, last = last, head
    #         while head!=[]:
    #             cur = head.pop()
    #             for i in range(len(wordList)-1, -1, -1):
    #                 j=wordList[i]
    #                 if self.isConnect(cur, j):
    #                     if j in last:
    #                         return ans
    #                     stack2.append(j)
    #                     wordList.pop(i)
    #             if head == []:
    #                 ans += 1 
    #                 head = stack2
    #                 stack2 = []
    #     return 0

    # def isConnect(self, Word1, Word2):
    #     count = 0
    #     for i in range(len(Word1)):
    #         if Word1[i] != Word2[i]:
    #             count += 1
    #     return count == 1