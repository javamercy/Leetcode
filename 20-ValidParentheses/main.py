class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"[": "]", "{": "}", "(": ")"}

        for c in s:
            if c in d:
                stack.append(c)
                continue

            if len(stack) == 0:
                return False

            if d[stack.pop()] != c:
                return False

        return len(stack) == 0
