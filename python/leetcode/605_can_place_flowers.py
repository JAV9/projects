'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

 

Constraints:

    1 <= flowerbed.length <= 2 * 104
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length


Solution planning:
    1. 3 consecutive zeroes = flower can be planted
    2. at i = 0, the left position count as zero (so, zeroes = 1)
    3. at i = len(flowerbed) - 1, the right position count as zero (so, zeroes += 1)
       OR we can check if zeroes == 2, plus the zero of the right -> flower can be planted
    4. traverse the array and return True if there are not remaining flowers to be planted
'''

from typing import List

class Solution:
   def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        zero = 1
        while cnt < len(flowerbed) and n > 0:
            if flowerbed[cnt] == 0:
                zero += 1
            else:
                zero = 0

            if zero == 3:
                n -= 1
                zero = 1
                
            cnt += 1

        if zero == 2 and n > 0:
            n -= 1

        return n == 0

        
fb = [1,0,0,0,1]
n = 1
Solution().canPlaceFlowers(fb, n)