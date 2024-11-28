class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_letters = "aeiou"
        current_count = sum(1 for char in s[:k] if char in vowel_letters)
        max_count = current_count

        for i in range(k, len(s)):
            if s[i-k] in vowel_letters:
                current_count -= 1

            if s[i] in vowel_letters:
                 current_count += 1

            max_count = max(max_count, current_count)

        return max_count