# Problem: First element with unique frequency
# LeetCode #: 3843
# Difficulty: Medium
# Topic: Arrays, Hashing
# Approach: HashMap
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        d2 = {}
        for i in d:
            d2[d[i]] = d2.get(d[i], 0) + 1
        for i in nums:
            if d2[d[i]] == 1:
                return i
        return -1
            
        