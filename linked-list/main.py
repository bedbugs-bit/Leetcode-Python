from add_new_numbers import ListNode, addTwoNumbers

# Creating linked lists for l1 = [2, 4, 3] and l2 = [5, 6, 4].
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

result = addTwoNumbers(l1, l2)

# Print out the result
output = []
while result:
    output.append(result.val)
    result = result.next

print(output) # Output: [7, 0, 8]