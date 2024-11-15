def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Compare elements from both halves and merge them
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Append remaining elements from either half
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


