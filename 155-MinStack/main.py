class MinStack1:
    def __init__(self):
        self.stack: list[tuple[int, int]] = []

    def push(self, val: int) -> None:
        min_val: int
        if len(self.stack) > 0:
            min_val = self.stack[-1][0]
            if val < min_val:
                min_val = val
        else:
            min_val = val
        self.stack.append((min_val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][1]

    def getMin(self) -> int:
        return self.stack[-1][0]


class MinStack2:
    def __init__(self):
        self.val_stack: list[int] = []
        self.min_stack: list[int] = []

    def push(self, val: int) -> None:
        self.val_stack.append(val)
        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.val_stack.pop()
        if self.min_stack[-1] == val:
            self.min_stack.pop()

    def top(self) -> int:
        return self.val_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
