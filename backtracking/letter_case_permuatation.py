from typing import List


class Solution:
    def iterative_solu(self, s: str) -> List[str]:
        output = []
        for char in s:
            temp = []
            if char.isalpha():
                for val in output:
                    temp.append(val + char.lower())
                    temp.append(val + char.upper())
            else:
                for val in output:
                    temp.append(val + char)
            output = temp

        # O(2**n) time because of the 2 permutations for a char
        # O(2**n) space

        return output

    def letterCasePermutation(self, s: str) -> List[str]:
        result = []

        def backtrack_recursive(index: int, path: List[str]):
            # base case, if we reach the end, add the current permutation

            if index == len(s):
                result.append("".join(path))
                return

            char = s[index]

            # add the char as is (if digit, just continue)
            path.append(char)
            backtrack_recursive(index + 1, path)
            path.pop # backtrack

            # if it's a char, toggle the case
            if char.isalpha():
                path.append(char.swapcase()) # change the case
                backtrack_recursive(index + 1, path)
                path.pop() # backtrack

        backtrack_recursive(0, [])

        # 0(2**n  * n) time; the join operation run in O(n) that's what cause the extra complexity
        # 0(2**n  * n) space
        return result


