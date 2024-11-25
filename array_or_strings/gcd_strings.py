from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # check if str1 + str2 is the same as  str2 + str1
        if str1 + str2 != str2 + str1:
            return ""

        # find the gcd of the lengths
        gcd_length = gcd(len(str1), len(str2))

        return str1[:gcd_length]

    def brute_force_gcdOfStrings(self, str1: str, str2: str) -> str:

        def repeats(string, sub_str):
            return string == sub_str * (len(string)//len(sub_str))

        min_len = min(len(str1), len(str2))

        for i in range(min_len, 0, -1):
            # check if the length i can be a divisor for both str1 and str2
            if len(str1) % i == 0 and len(str) % i == 0:
                candidate = str1[:i]
                if repeats(str1, candidate) and repeats(str2, candidate):
                    return candidate

        return ""



