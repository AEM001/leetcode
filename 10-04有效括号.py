class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 !=0:
            return False
        if not s:
            return True
        stack=[]
        for i in s:
            if i=='('or i=='['or i=='{':
                stack.append(i)
            if i==')':
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    return False
            elif i==']':
                if stack and stack[-1]=='[':
                    stack.pop()
                else:
                    return False
            elif i=='}':
                if stack and stack[-1]=='{':
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True

            