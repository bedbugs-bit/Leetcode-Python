from collections import deque

from setuptools.command.dist_info import dist_info


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        r_queue = deque()
        d_queue = deque()

        for index, senator in enumerate(senate):
            if senator == 'R':
                r_queue.append(index)
            else:
                d_queue.append(index)

        # simulate the rounds between both types of senators
        while r_queue and d_queue:
            r_index = r_queue.popleft()
            d_index = d_queue.popleft()

            if r_index < d_index:
                r_queue.append(r_index + n)
            else:
                d_queue.append(d_index + n)

        return "Radiant" if r_queue else "Dire"

