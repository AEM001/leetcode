class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # def generate(num:str,i:int):
        #     count=0
        #     final=[]
        #     while i>0:
        #         if num[i]=="#":
        #             count+=1
        #             i-=1
        #         else:
        #             if i-count <0:
        #                 return final
        #             i-=count
        #             final.append(num[i])
        #             count=0
        #     return final
        # return generate(s,len(s)-1)==generate(t,len(t)-1)
        def generate(num):
            num=list(num)
            stack=[]
            for i in num:
                if i !="#":
                    stack.append(i)
                else:
                    stack.pop()
            "".join(stack)
        return generate(s)==generate(t)
    
    class Solution:
        def backspaceCompare(self, s: str, t: str) -> bool:
            def process_string(string: str) -> str:
                stack = []
                for char in string:
                    if char != "#":
                        stack.append(char)
                    elif stack:  # 如果栈不为空，弹出最后一个字符
                        stack.pop()
                return "".join(stack)
            
            return process_string(s) == process_string(t)
    class Solution:
        def backspaceCompare(self, s: str, t: str) -> bool:
            def generate(num):
                final=[]
                count=0
                for i in range(len(num)-1,-1,-1):
                    if num[i]=="#":
                        count+=1
                    elif count>0:
                        count-=1
                    else:
                        final.append(num[i])
                return "".join(final[::-1])
            return generate(s)==generate(t)