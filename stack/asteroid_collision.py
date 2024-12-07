from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                diff = asteroid + stack[-1]
                if diff < 0:  # Current asteroid destroys the stack top
                    stack.pop()
                elif diff > 0:  # Stack top destroys the current asteroid
                    asteroid = 0
                else:  # Both asteroids destroy each other
                    asteroid = 0
                    stack.pop()

            # Only append the asteroid if it survives
            if asteroid:
                stack.append(asteroid)

        return stack
