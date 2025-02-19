def stack_sorting_iterative(stack):
    temp_stack = []

    while stack:
        num = stack.pop()

        # ascending order
        while temp_stack and (temp_stack[-1] > num):
            stack.append(temp_stack[-1])
            temp_stack.pop()

        temp_stack.append(num)

    return temp_stack

