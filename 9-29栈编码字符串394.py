class Solution:
    def decodeString(self, s: str) -> str:
        num,letter,stack=0,"",[]
        for i in s:
            if i=="[":
                stack.append([num,letter])
                num,letter=0,""
            elif i=="]":
                cur_num,last_letter=stack.pop()
                letter=last_letter+cur_num*letter
            elif '0'<=i<='9':
                num=num*10+int(i)
            else:
                letter+=i
        return letter

#找到pattern，一种感觉，确定需要的数据结构和变量，将思路使用变量和逻辑关系联系起来