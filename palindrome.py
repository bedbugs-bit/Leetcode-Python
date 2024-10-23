class Solution:

    def string_palindrome(self, s: str) -> bool:
        # Remove non-alphanumerics
        cleaned_s = ''.join(char.lower() for char in s if char.isalnum())

        left, right = 0, len(cleaned_s)-1

        while left < right:
            if cleaned_s[left] != cleaned_s[right]:
                return False
            left += 1
            right -= 1

        return True

    def longest_palindrome(self, s: str) -> str:
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1 : right]

        if len(s) == 0:
            return ""

        longest = ""

        for i in range(len(s)):
            # check for odd-length palindrome (single char center)
            palindrome_odd = expand_around_center(i, i)

            # check for even-lenght palindromes (double center)
            palindrome_even = expand_around_center(i, i+1)

            longest = max(longest, palindrome_even, palindrome_odd, key=len)

        return longest

    def count_substrings(self, s: str) -> int:
        if len(s) == 0:
            return 0

        def count_palindrome_from_center(left, right):
            result = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                result += 1
            return result

        total_palindrome = 0

        for i in range(len(s)):
            # check for palindrome of odd-length(single char center)
            total_palindrome += count_palindrome_from_center(i,i)
            total_palindrome += count_palindrome_from_center(i, i+1)

        return total_palindrome


