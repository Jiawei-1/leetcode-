class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic={}


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        dic=self.dic
        for char in word:
            if char not in dic:
                dic[char]={}
            dic=dic[char]
        dic['end']=True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        dic=self.dic
        for char in word:
            if char not in dic:
                return False
            dic=dic[char]
        if 'end' in dic:
            return True
        else:
            return False



    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        dic=self.dic
        for char in prefix:
            if char not in dic:
                return False
            dic=dic[char]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)