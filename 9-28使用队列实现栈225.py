from collections import deque
class MyStack:

    def __init__(self):
        self.s1=deque()
        self.s2=deque()

    def push(self, x: int) -> None:
        self.s2.append(x)
        while self.s1:
            temp=self.s1.popleft()
            self.s2.append(temp)
        self.s1,self.s2=self.s2,self.s1
        

    def pop(self) -> int:
        if self.empty():
            return None
        return self.s1.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        return self.s1[0]
        

    def empty(self) -> bool:
        return len(self.s1)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()