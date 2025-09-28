class MinStack:
    def __init__(self):
        self.stack=[]
        self.ministack=[]
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        # if not self.ministack or val<self.ministack[-1]:
        if not self.ministack or val<=self.ministack[-1]:
            self.ministack.append(val)
    
    def pop(self) -> None:
        if self.stack:
            val=self.stack.pop()#不知道这个用法
            if val==self.ministack[-1]:
                self.ministack.pop()

    def top(self) -> int:
        # if self.stack:
        #     return 
        return self.stack[-1]
    
    def getMin(self) -> int:
        # if self.stack:
        #     return
        return self.ministack[-1]
        


        