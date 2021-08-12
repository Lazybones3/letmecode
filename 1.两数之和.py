#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if diff in d:
                return [d[diff], i]
            else:
                d[num] = i
        return []
# @lc code=end

