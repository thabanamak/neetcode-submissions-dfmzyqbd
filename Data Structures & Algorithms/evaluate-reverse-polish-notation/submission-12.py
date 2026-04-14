class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        op = ["+","-","*","/"]
        for s in tokens:
            if s not in op:
                stack.append(int(s))
            else:
                second = stack.pop()
                first = stack.pop()
                
                if s == "+":
                    stack.append(first + second)
                elif s == "-":
                    stack.append(first - second)
                elif s == "*":
                    stack.append(first * second)
                elif s == "/":
                    stack.append(int(first / second))
        return stack[-1]
                


            
        