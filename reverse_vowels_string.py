class Solution:
    def reverseVowels(self, s: str) -> str:
        word = list(s)
        start = 0
        end = len(s) - 1
        vowels = set("aeiouAEIOU")

        while start < end:
            # Advance start if not a vowel
            if word[start] not in vowels:
                start += 1
                continue  # Go to the next iteration without further checks

            # Advance end if not a vowel
            if word[end] not in vowels:
                end -= 1
                continue

            # Both word[start] and word[end] are vowels; swap and move both pointers
            word[start], word[end] = word[end], word[start]
            start += 1
            end -= 1

        return ''.join(word)

    def reverse_vowels_fast(self, s: str)->str:
        vowels = [char for char in s if char in "aeiouAEIOU"]

        word = [char if char not in 'aeiouAEIOU' else vowels.pop() for char in s]

        return ''.join()
