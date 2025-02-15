# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        curr_node = dummy_head

        while curr_node.next != None:
            if curr_node.next.val == val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next
        # O(n) time, 0(1) space
        return dummy_head.next



