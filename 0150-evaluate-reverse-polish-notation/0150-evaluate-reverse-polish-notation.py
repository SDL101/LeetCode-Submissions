class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "*":
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)
            elif token == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first/second)) #round any dec vals toward 0. (can use int() or math.trunc(), not same as round down since neg/pos)
            elif token == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)
            elif token == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            else:
                stack.append(int(token))  #make sure to type cast to int and don't add the str version to stack

        return stack[0]

    # Time Complexity: O(n) - looping through the whole tokens arr
    # Space Complexity: O(n) - stack scales linearly with the size of the tokens arr