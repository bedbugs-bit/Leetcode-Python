class Solution:
    def merge_alternately(self, word1: str, word2: str) -> str:
        merged = []
        length1, length2 = len(word1), len(word2)

        min_length = min(length1, length2)

        # Iterate up to the length of the shorter word
        for i in range(min_length):
            merged.append(word1[i])
            merged.append(word2[i])

        # Append remaining characters from the longer word
        if length1 > length2:
            merged.append(word1[length2:])
        else:
            merged.append(word2[length1:])

        return ''.join(merged)