class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = [(target - p, (target - p) / s) for p, s in zip(position, speed)]
        cars = sorted(cars, key=lambda x: x[0])
        stack = []

        for car in cars:
            if not stack:
                stack.append(car)
                continue

            if car[1] > stack[-1][1]:
                stack.append(car)

        return len(stack)
