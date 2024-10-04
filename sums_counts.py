def sum_of_n_natural_numbers(n):
    # 1, 2, 3, 4

    return n *(n+1) // 2


def prefix_sum(arr):
    # arr is an array

    size = len(arr)
    prefix_A = [0] * size

    for i in range(1, size +1):
        prefix_A[i] = prefix_A[i-1] + arr[i-1]
        

def count_num_occurrence(arr):
    # count the number of occurrence of numbers in an array
    # arr is an array
    size = len(arr)
    count_arr = [0] * size

    for val in arr:
        count_arr[val] += 1

    return count_arr







