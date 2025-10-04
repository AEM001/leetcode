class Solution:
    def calculate(self, s: str) -> int:
        size = len(s)
        stack = []      # 用于存储每一步的中间结果
        op = '+'        # 记录上一个运算符，初始为加号
        index = 0
        while index < size:
            if s[index] == ' ':
                # 跳过空格
                index += 1
                continue
            if s[index].isdigit():
                # 解析多位数字
                num = ord(s[index]) - ord('0')
                while index + 1 < size and s[index+1].isdigit():
                    index += 1
                    num = 10 * num + ord(s[index]) - ord('0')
                # 根据上一个运算符进行处理
                if op == '+':
                    stack.append(num)         # 加号直接入栈
                elif op == '-':
                    stack.append(-num)        # 减号取相反数入栈
                elif op == '*':
                    top = stack.pop()         # 乘法弹出栈顶元素
                    stack.append(top * num)   # 计算后入栈
                elif op == '/':
                    top = stack.pop()         # 除法弹出栈顶元素
                    # Python 的 int() 向零取整，符合题意
                    stack.append(int(top / num))
            elif s[index] in "+-*/":
                # 更新当前运算符
                op = s[index]
            index += 1
        # 栈中所有元素求和即为最终结果
        return sum(stack)