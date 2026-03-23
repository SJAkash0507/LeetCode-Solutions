# Problem: Two Sum
# LeetCode #: 1
# Difficulty: Easy
# Topic: Arrays, Hashing
# Approach: HashMap
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = []
        d = {}
        for i in range(0, len(nums)):
            v = target - nums[i]
            if v in d.keys():
                s.append(d[v])
                s.append(i)
            else:
                d[nums[i]] = i
        return s

        