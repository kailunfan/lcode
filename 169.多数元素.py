#
# @lc app=leetcode.cn id=169 lang=python
#
# [169] 多数元素
#
# https://leetcode-cn.com/problems/majority-element/description/
#
# algorithms
# Easy (62.96%)
# Likes:    626
# Dislikes: 0
# Total Accepted:    175K
# Total Submissions: 275.7K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 
# 
# 
# 示例 1:
# 
# 输入: [3,2,3]
# 输出: 3
# 
# 示例 2:
# 
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
# 
# 
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 投票法
        count = 0
        candicate = None
        for item in nums:
            if candicate == item:
                count += 1
                continue
            count -= 1
            if count < 0:
                candicate = item
                count = 1
        return candicate
# @lc code=end

