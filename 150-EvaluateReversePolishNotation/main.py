class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators: set[str] = {"+", "-", "*", "/"}
        stack: list[int] = []
        for token in tokens:
            if token in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                res: int

                if token == "+":
                    res = num1 + num2
                elif token == "/":
                    res = int(num1 / num2)
                elif token == "*":
                    res = num1 * num2
                else:
                    res = num1 - num2

                stack.append(res)
            else:
                stack.append(int(token))

        return stack.pop()
