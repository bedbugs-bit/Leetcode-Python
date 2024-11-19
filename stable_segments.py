def countStableSegments(capacity):
    num_servers = len(capacity)
    prefix_sum = [0] * (num_servers + 1)

    # Compute prefix sum
    for i in range(num_servers):
        prefix_sum[i + 1] = prefix_sum[i] + capacity[i]

    stable_sub_segment_count = 0

    # Iterate over all possible start indices
    for start_index in range(num_servers):
        # Expand the end index for subsegments of length >= 3
        for end_index in range(start_index + 2, num_servers):
            # Check if the first and last elements are equal
            if capacity[start_index] != capacity[end_index]:
                continue

            # Calculate the interior sum using the prefix sum array
            interior_sum = prefix_sum[end_index] - prefix_sum[start_index + 1]

            # Check if the subsegment is stable
            if capacity[start_index] == interior_sum:
                stable_sub_segment_count += 1

            # Stop expanding if the interior sum exceeds the first element
            if interior_sum > capacity[start_index]:
                break

    return stable_sub_segment_count


# Example usage
capacity = [9, 3, 1, 2, 3, 9, 10]
print(countStableSegments(capacity))  # Output: 1
