class MyCircularDeque:

    def __init__(self, k: int):
        self.queue=[0]*(k+1)
        self.front=0
        self.rear=0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.front]=value
        self.front=(self.front-1)%len(self.queue)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear=(self.rear+1)%len(self.queue)
        self.queue[self.rear]=value
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front=(self.front+1)%len(self.queue)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear=(self.rear-1)%len(self.queue)
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.front+1)%len(self.queue)]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.front==self.rear

    def isFull(self) -> bool:
        return self.front==(self.rear+1)%len(self.queue)


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()