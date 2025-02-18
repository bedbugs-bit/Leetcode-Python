from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char not in "+-*/":
                stack.append(int(char))

            else:
                left, right = stack.pop(), stack.pop()
                if char == '-':
                    stack.append(left - right)
                elif char == '+':
                    stack.append(left + right)
                elif char == '*':
                    stack.append(left * right)
                else:
                    stack.append(left//right)

        return stack.pop()



