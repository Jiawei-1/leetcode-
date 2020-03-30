class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l1=list()
        self.l2=list()


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.l1.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len (self.l2)==0:
            while self.l1:
                self.l2.append(self.l1.pop())
        return self.l2.pop()


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len (self.l2)==0:
            while self.l1:
                self.l2.append(self.l1.pop())
        return self.l2[-1]



    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.l1)==0 and len(self.l2)==0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()