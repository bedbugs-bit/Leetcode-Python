# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # create a dummy node
        dummy = ListNode(0)
        # dummy should point to head
        dummy.next = head
        prev = dummy

        # Step 2: Move prev to the node before 'left-th' node
        for _ in range(left - 1):
            prev = prev.next # prev now point to the node before the left position

        # Step 3: Reverse nodes from left to right
        curr = prev.next
        temp = None

        for _ in range(right - left + 1): # the number of nodes to be reversed
            next_node = curr.next
            curr.next = temp # reverse link
            temp = curr
            curr = next_node

        # Step 4: Connect the reversed part back to list
        prev.next.next = curr
        prev.next = temp

        # O(n) time, O(1) space complexity
        return dummy.next # return the new head




