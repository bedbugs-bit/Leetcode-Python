# Definition for singly-linked list.
from typing import Optional
from unittest.mock import right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # Three part solution
        # Find the middle of the linked list
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow= slow.next

        # Reverse the second half of the linked list
        temp = None # placeholder node for reversing thre linked list
        while slow !=None: # slow point to the middle of the palindrome
            next_pointer = slow.next
            slow.next = temp
            temp = slow
            slow = next_pointer

        # check if palindrome with two pointer
        left = head
        right = temp

        while right != None:
            if left.val != right.val:
                return False # Not a palindrome

            left = left.next
            right = right.next

        return True









