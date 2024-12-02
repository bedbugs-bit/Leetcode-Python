class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # check if the length of both strings are the same
        if len(word1) != len(word2):
            return False

        freq1 = {}
        freq2 = {}

        # count the frequency of chars in both words
        for char in word1:
            freq1[char] = freq1.get(char, 0) + 1

        for char in word2:
            freq2[char] = freq2.get(char, 0) + 1

        if freq2.keys() != freq1.keys():
            return False

        if set(word1) != set(word2):
            return False

        return sorted(freq1.values()) == sorted(freq2.values())


