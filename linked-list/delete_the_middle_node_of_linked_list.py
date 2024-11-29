class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteMiddle(self, head):

        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # if the list has one Node or is empty
        if not head or not head.next:
            return None

        slow, fast = head, head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = slow.next

        return head

