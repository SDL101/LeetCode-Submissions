class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # dont forget to round down on division - use floor() 
        stack = []

        for token in tokens:
            if token == "*":
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)
            elif token == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first/second))
            elif token == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)
            elif token == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            else:
                stack.append(int(token)) 

        return stack[0]