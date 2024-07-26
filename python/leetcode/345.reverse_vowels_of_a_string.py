'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"

Example 2:

Input: s = "leetcode"
Output: "leotcede"

 

Constraints:

    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.


'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s)-1
        s_list = list(s)
        vowels = "aeiouAEIOU"
        while i < j:
            if s_list[i] not in vowels:
                i += 1
            elif s_list[j] not in vowels:
                j -= 1
            else: 
                s_list[i], s_list[j] = s_list[j], s_list[i]     # swap
                i += 1
                j -= 1
        return ''.join(s_list)