class Solution:
    def climbing_stairs(self, n: int):
        # n is 4
        # [0, 1, 2, 3]
        # [3, 2, 1, 1]
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one
