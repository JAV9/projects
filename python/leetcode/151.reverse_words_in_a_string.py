'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

 

Constraints:

    1 <= s.length <= 104
    s contains English letters (upper-case and lower-case), digits, and spaces ' '.
    There is at least one word in s.

'''
class Solution:
    def reverseWords(self, s: str) -> str:
        ret = []
        word = []
        n = len(s)
        i = 0

        # parse the string to extract words
        while i < n:
            if s[i] != ' ':
                word.append(s[i])
            else:
                if word:
                    ret.append(''.join(word))
                    word = []
            i += 1

        # add the last word if there is any
        if word:
            ret.append(''.join(word))

        # reverse the list of words
        i, j = 0, len(ret) -1
        while i < j:
            ret[i], ret[j] = ret[j], ret[i]
            i += 1
            j -= 1

        # construct the final string
        result = []
        for word in ret:
            if result:
                result.append(' ')
            result.append(word)

        return ''.join(result)