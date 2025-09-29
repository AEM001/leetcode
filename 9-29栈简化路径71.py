class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        for i in path:
            if i=="/" and len(stack)!=0:
                if stack[-1]=="/":
                    stack.pop()
                    stack.append(i)
                elif stack[-1]=="."and stack[-2]=="."and stack[-3]=="/":
                    for j in range(4):
                        stack.pop()
                    if len(stack)==0:
                        stack.append(i)
                    else:
                        while(stack[-1]!="/"):
                            stack.pop()
                        stack.pop()
                        stack.append(i)
                elif stack[-1]=='.'and stack[-2]=='/':
                    for j in range(2):
                        stack.pop()
            else:
                stack.append(i)
        return "".join(stack)

                
