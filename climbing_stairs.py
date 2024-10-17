from typing import List


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

    def min_cost_climbing_stairs_recursive(self, cost_arr, num_steps):
        """
        :param cost_arr: The integer array cost, where cost[i] is the cost of the i-th step on a staircase
        :param num_steps: The number of steps in the staircase
        :return: minimum cost to reach the top
        """

        if num_steps < 0:
            return 0

        if num_steps == 0 or num_steps == 1:
            return cost_arr[num_steps]

        # Take the min of climbing from one step before or two steps before

        return cost_arr[num_steps] + min(self.min_cost_climbing_stairs_recursive(cost_arr, num_steps - 1),
                                         self.min_cost_climbing_stairs_recursive(cost_arr, num_steps - 2))

    def min_cost_climbing_stairs_dynamic_programming(self, cost_arr: List[int]):

        """
        :param cost_arr: The integer array cost, where cost[i] is the cost of the i-th step on a staircase
        :return: minimum cost to reach the top
        """

        if len(cost_arr) == 1 or 2:
            return cost_arr[0]

        cost_arr.append(0)

        for i in range(len(cost_arr) -3, -1, -1):
            cost_arr[i] += min(cost_arr[i+1], cost_arr[i+2])

            return min(cost_arr[0], cost_arr[1])


    def min_cost_climbing_stairs_memoization(self, cost_arr):
        """
        :param cost_arr: The integer array cost, where cost[i] is the cost of the i-th step on a staircase.
        :return: Minimum cost to reach the top.
        """

        # Dict/hash map to store the min cost for each step
        memo ={}

        # Base case
        if len(cost_arr) == 0:
            return 0

        if len(cost_arr) == 1:
            return cost_arr[0]

        # If the last step result is already computed, return it

        if len(cost_arr) in memo:
            return memo[len(cost_arr)]

        # Memoize approach
        if len(cost_arr) == 2:
            memo[len(cost_arr)] = min(cost_arr[0], cost_arr[1])
            return memo[len(cost_arr)]

        memo[len(cost_arr)] = min(self.min_cost_climbing_stairs_memoization(cost_arr[:-1]) + cost_arr[-1],
                                  self.min_cost_climbing_stairs_memoization(cost_arr[:-2]) + cost_arr[-2])

        return memo[len(cost_arr)]

        

