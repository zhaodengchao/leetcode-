'''设计循环队列'''
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.__size = k
        self.head = 0
        self.tail = 0
        self.num = 0
        self.queue = [None]*self.__size

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.num > self.__size-1:
            return False
        else:
            if self.isEmpty():
                self.queue[self.tail] = value
            else:
                if self.tail+1 <= self.__size-1:
                    self.queue[self.tail+1]=value
                    self.tail += 1
                else:
                    self.tail = 0
                    self.queue[self.tail] = value
            self.num += 1
            return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            if self.head==self.tail:
                self.queue[self.head]=None
            else:
                self.queue[self.head]=None
                self.head += 1
                if self.head > self.__size-1:
                    self.head = 0
            self.num -= 1
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.head]       

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.tail]       

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.num == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.num == self.__size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
