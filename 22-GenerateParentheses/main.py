class Solution:
    def generateParenthesis1(self, n: int) -> list[str]:
        s: set[str] = {"()"}
        for k in range(1, n):
            sub_s: set[str] = set()
            for val in s:
                for i in range(len(val)):
                    new_val = val[:i + 1] + "()" + val[i + 1:]
                    sub_s.add(new_val)
                sub_s.add("(" * (k + 1) + ")" * (k + 1))
                sub_s.add("(" + val + ")")
            s = sub_s
        return list(s)

    def generateParenthesis2(self, n: int) -> list[str]:
        stack = []
        result = []

        def backtrack(num_open, num_closed):
            if num_open == n == num_closed:
                result.append("".join(stack))

            if num_open < n:
                stack.append("(")
                backtrack(num_open + 1, num_closed)
                stack.pop()

            if num_closed < num_open:
                stack.append(")")
                backtrack(num_open, num_closed + 1)
                stack.pop()

        backtrack(0, 0)
        return result
