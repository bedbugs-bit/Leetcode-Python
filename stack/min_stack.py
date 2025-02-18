class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # Determine the new min value correctly
        if not self.stack:
            curr_min = val  # First element is the minimum
        else:
            curr_min = min(val, self.stack[-1][1])  # Compare with current min
        # Store (value, current minimum) as a tuple
        self.stack.append((val, curr_min))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None
