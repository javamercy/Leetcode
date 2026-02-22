class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answers = [0] * len(temperatures)
        stack: list[tuple[int, int]] = []
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, idx = stack.pop()
                answers[idx] = i - idx

            stack.append((temp, i))

        return answers
