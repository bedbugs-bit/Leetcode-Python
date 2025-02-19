from collections import deque

class Solution:
    # brute force solution
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        q = deque([(i, tickets[i]) for i in range(len(tickets))])
        time = 0

        while q:
            index, remaining = q.popleft() # person buys 1 ticket
            time += 1 # Increment time
            remaining -= 1 # reduce the ticket count

            if remaining > 0:
                q.append((index, remaining))
            if index == k and remaining == 0:
                return time
            # O(n * m), m ticket for position k, n people
    # optimised solution
    def solu_optimised_time_required_to_buy(self, tickets: list[int], k: int) -> int:
        total_time = 0
        for i in range(len(tickets)):
            if i <= k:
                total_time += min(tickets[i], tickets[k])
            else:
                total_time += min(tickets[i], tickets[k] - 1 )

        return total_time

