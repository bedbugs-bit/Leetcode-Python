# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # Initialize a dummy node to simplify the code.
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0  # Initialize carry to 0.

    # Traverse both lists until both are exhausted and there's no carry left.
    while l1 or l2 or carry:
        # Get the values from the current nodes of l1 and l2 (or 0 if one list is shorter).
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate the sum of the values and the carry.
        total = val1 + val2 + carry
        carry = total // 10  # Update the carry for the next iteration.
        new_val = total % 10  # The value for the current node.

        # Add the computed value as a new node to the result list.
        current.next = ListNode(new_val)
        current = current.next

        # Move to the next nodes in l1 and l2 if they exist.
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    # Return the head of the resulting list.
    return dummy_head.next
