from email.utils import parsedate_to_datetime


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

    def count_total_palindrome_substrings(self, s: str) -> int:
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


    def break_palindrome(self, palindrome_string):

        if len(palindrome_string) == 1:
            return 'IMPOSSIBLE'

        # Convert the string to a list to allow modification
        chars = list(palindrome_string)
        size = len(chars)

        # Try to make the smallest possible change in the first half
        for i in range(size//2):
            if chars[i] != 'a':
                chars[i] = 'a'
                return ''.join(chars)

        # if all characters in the first half are 'a', change the last character to 'b'
        # in lexicography, the leftmost char have the greater weight,
        # so to minimize the lexicographical number
        # we change numbers on the leftmost part to the smallest value 'a'.
        # to increase the lexicographical number, we add a small value 'b' to the rightmost part
        chars[-1] = 'b'
        return ''.join(chars)






