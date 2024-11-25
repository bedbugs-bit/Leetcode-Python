from typing import List

class Solution:

    def house_robber(self, houses: List[int]) -> int:

        """
            :param nums: List[int] representing money in each house.
            :return: int representing the maximum money that can be robbed.
        """
        rob1, rob2 = 0

        # [rob1, rob2, house]
        # [1, 2, 1, 4]


        for house in houses:
            temp = max(house + rob1, rob2)
            rob1 = rob2
            rob2 = temp


        return rob2

    def house_robber_recursive(self, houses: List[int]) -> int:
        """
        :param nums: List[int] representing money in each house.
        :return: int representing the maximum money that can be robbed.
        """
        def helper(house, current_index):
            if current_index >= len(house):
                return 0

            # recursion
            rob_current = house[current_index] + helper(house, current_index + 2)
            skip_current = helper(house, current_index + 1)

            return max(rob_current, skip_current)

        return helper(houses, 0)

    def house_robber_2(self, houses: List[int]) -> int:
        """
        :param houses: List[int] representing money in each house.
        :return: int representing the maximum money that can be robbed.
        """

        def helper(houses):

            rob1, rob2 = 0, 0

            for house in houses:

                new_rob = max(rob1 + house, rob2)
                rob1 = rob2
                rob2 = new_rob

            return rob2

        return max(houses[0], helper(houses[1:]), helper(houses[:-1]))









