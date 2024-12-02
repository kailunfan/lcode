#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# https://leetcode-cn.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (40.20%)
# Likes:    780
# Dislikes: 0
# Total Accepted:    89.9K
# Total Submissions: 223.4K
# Testcase Example:  '[1,2,0]'
#
# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
# 
# 
# 
# 示例 1:
# 
# 输入: [1,2,0]
# 输出: 3
# 
# 
# 示例 2:
# 
# 输入: [3,4,-1,1]
# 输出: 2
# 
# 
# 示例 3:
# 
# 输入: [7,8,9,11,12]
# 输出: 1
# 
# 
# 
# 
# 提示：
# 
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
# 
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        state = [0]*(len(nums)+1)
        for i in nums:
            if 0<=i<len(state):
                state[i] = 1
        for idx, i in enumerate(state):
            if idx>0 and i == 0:
                return idx
        return len(state)


# @lc code=end

