from collections import defaultdict

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

    def distinct_palindrome(self, s):
        """
        Solution:
        - Use a set data structure to count distict palidromes
        - Create a function to expand around the centre to take care of odd and even palindromes

        """

        def count_from_centre(left, right):
            result = set()
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                result.add(s[left:right + 1])
                left -= 1
                right += 1

            return result

        distinct_palindromes = set()

        for i in range(len(s)):
            distinct_palindromes.update(count_from_centre(i, i))
            distinct_palindromes.update(count_from_centre(i, i + 1))

        return len(distinct_palindromes)


    def break_palindrome(self, palindrome_string):

        if len(palindrome_string) == 1:
            return 'IMPOSSIBLE'

        # Convert the string to a list to allow modification
        chars = list(palindrome_string)
        size = len(chars)

        # Try to make a change to make the string as small as possible so start with the first half
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

    def getMaxOccurrences(self, components, minLength, maxLength, maxUnique):
        """

        Solution

        - iterate at the starting index whilst expanding the substring to the maxLength
        - added helper function to implement set data structure ensuring unique chars and a function to return a bool if a substring is valid

        - time complexity of O(n), space complexity of O(n^2)
        """
        # Write your code here
        substring_count = defaultdict(int)

        def count_unique_chars(substring):
            return len(set(substring))

        def is_valid_substring(substring):
            if len(substring) < minLength or len(substring) > maxLength:
                return False
            if count_unique_chars(substring) > maxUnique:
                return False

            return True

        for i in range(len(components)):
            substr = ""

            for j in range(i, min(len(components), i + maxLength)):
                substr += components[j]

                if is_valid_substring(substr):
                    substring_count[substr] += 1

        return max(substring_count.values(), default=0)


