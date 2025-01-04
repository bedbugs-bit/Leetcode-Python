# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Optional:
    pass


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list is empty or has only one node, no reordering is needed.
        if not head or not head.next:
            return head

        # Initialize odd and even pointers
        odd = head  # Points to the first node (odd index)
        even = head.next  # Points to the second node (even index)
        even_head = even  # Store the head of the even-indexed list

        # Traverse and rearrange the list
        while even and even.next:
            odd.next = even.next  # Link the next odd node
            odd = odd.next  # Move the odd pointer forward

            even.next = odd.next  # Link the next even node
            even = even.next  # Move the even pointer forward

        # Connect the end of the odd list to the head of the even list
        odd.next = even_head

        return head  # Return the reordered list
