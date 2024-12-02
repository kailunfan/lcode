#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#
# https://leetcode.cn/problems/third-maximum-number/description/
#
# algorithms
# Easy (39.73%)
# Likes:    435
# Dislikes: 0
# Total Accepted:    148.2K
# Total Submissions: 372.9K
# Testcase Example:  '[3,2,1]'
#
# 给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：[3, 2, 1]
# 输出：1
# 解释：第三大的数是 1 。
# 
# 示例 2：
# 
# 
# 输入：[1, 2]
# 输出：2
# 解释：第三大的数不存在, 所以返回最大的数 2 。
# 
# 
# 示例 3：
# 
# 
# 输入：[2, 2, 3, 1]
# 输出：1
# 解释：注意，要求返回第三大的数，是指在所有不同数字中排第三大的数。
# 此例中存在两个值为 2 的数，它们都排第二。在所有不同数字中排第三大的数为 1 。
# 
# 
# 
# 提示：
# 
# 
# 1 
# -2^31 
# 
# 
# 
# 
# 进阶：你能设计一个时间复杂度 O(n) 的解决方案吗？
# 
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        base = [float('-inf')]*3
        for n in nums:
            if n <= base[0]:
                continue
            if base[0]<n<=base[1]:
                base[0] = n
            elif base[1]<n<=base[2]:
                base[0],base[1] = base[1], n
            elif n>base[2]:
                base[0], base[1], base[2] = base[1],base[2], n
        return base[0]

# @lc code=end

