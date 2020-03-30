class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic={}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        dic=self.dic
        for char in key:
            if char not in dic:
                dic[char]={}
            dic=dic[char]
        dic['value']=val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        def search(dic,Sum):
            if not dic:
                return Sum
            if 'value' in dic:
                Sum+=dic['value']
            for char in dic:
                if char=='value':
                    continue
                Sum=search(dic[char],Sum)
            return Sum
        dic=self.dic
        Sum=0
        for char in prefix:
            if char not in dic:
                return Sum
            dic=dic[char]
        Sum=search(dic,Sum)
        return Sum
        
        
        
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)