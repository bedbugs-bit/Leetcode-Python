class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # iterative approach

    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            original_next_node = curr.next
            curr.next = prev
            prev = curr
            curr = original_next_node

        # time complexity of O(n) space complexity of O(1)
        return prev

    # recursive solution

    def recursive_reverse_list(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        reversed_head = self.recursive_reverse_list(head.next)
        head.next.next = head
        head.next = None

        return reversed_head




