class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.stack2=[]


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if len(self.stack2)==0 or self.stack2[-1]>x:
            self.stack2.append(x)
        else:
            self.stack2.append(self.stack2[-1])


    def pop(self):
        """
        :rtype: None
        """
        self.stack2.pop()
        return self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        
        return self.stack2[-1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()