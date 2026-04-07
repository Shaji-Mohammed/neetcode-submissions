class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result, a, b = 0, 0 ,0
        stack = []
        operators = {'+', "-", "*", "/"}

        for i in tokens:
            if i in operators:
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    stack.append(a + b)
                elif i == '-':
                    stack.append(b - a)
                elif i == '*':
                     stack.append(a * b)
                elif i == '/':
                    stack.append(int(b / a))
            else:
                stack.append(int(i))
                continue
            
        
        return stack[0]


