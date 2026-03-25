# Problem: Palindrome Number
# LeetCode #: 9
# Difficulty: Easy
# Topic: Math
# Approach: Reversal
# Time Complexity: O(log(n))
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = 0
        t = x
        while x > 0:
            r = x % 10
            a = (a * 10) + r
            x = x // 10
        if a == t:
            return True
        else : 
            return False
        