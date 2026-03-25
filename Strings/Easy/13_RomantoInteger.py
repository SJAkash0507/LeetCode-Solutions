# Problem: Roman to Interger
# LeetCode #: 13
# Difficulty: Easy
# Topic: Math, String
# Approach: HashMap
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        d =  {'I':1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D':500, 'M':1000}
        num = 0    
        for i in range(0, len(s)):
            if s[i] in d:
                num += d[s[i]]
            if i + 1 != len(s):
                if s[i] == 'I' and s[i + 1] in 'VX':
                    num -= 2
                elif s[i] == 'X' and s[i + 1] in 'LC':
                    num -= 20
                elif s[i] == 'C' and s[i + 1] in 'DM':
                    num -= 200
        return num