'''
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

 

Constraints:

    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters.

Plan for the solution:
    1. Check if str1 + str2 == str2 + str1. If not, there is no common divisor string.
    2. Find the GCD of the lengths of str1 and str2.
    3. The potential greatest common divisor string is the substring of length
       equal to this GCD from either str1 or str2
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        # euclidean alg, O(log(min(a,b)))
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if str1 + str2 != str2 + str1:
            return ""

        # determine the max possible len of the str that can be common divisor of both
        gcd_len = gcd(len(str1), len(str2))

        return str1[:gcd_len]