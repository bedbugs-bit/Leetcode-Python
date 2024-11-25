from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        write_index = 0  # pointer for where to put the compressed characters
        read_index = 0  # pointer to traverse the array

        while read_index < len(chars):
            char = chars[read_index]
            count = 0  # count the occurrences of this character

            # count all consecutive occurrences of the current character
            while read_index < len(chars) and chars[read_index] == char:
                read_index += 1
                count += 1

            # put the character to the write_index
            chars[write_index] = char
            write_index += 1

            # If count > 1, write the count as well
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1

        return write_index
