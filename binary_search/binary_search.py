from typing import List

def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        # double slash for integer division in Python 3
        # we don't have to worry about integer 'left + right' overflow
        # Python integers are arbitrarily large
        mid = left + right // 2
        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1 # if we get here we didn't hit the above return so we didn't find a target


if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = binary_search(arr, target)
    print(res)

