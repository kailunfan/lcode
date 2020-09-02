#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] x 的平方根
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (37.63%)
# Likes:    349
# Dislikes: 0
# Total Accepted:    118K
# Total Submissions: 313.5K
# Testcase Example:  '4'
#
# 实现 int sqrt(int x) 函数。
# 
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
# 
# 示例 1:
# 
# 输入: 4
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
# 由于返回类型是整数，小数部分将被舍去。
# 
# 
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 暴力
        # i = 0 
        # while True:
        #     if i**2>x:
        #         return i-1
        #     i += 1
        # 二分法
        l,r,ans = 0,x,-1
        while l<=r:
            mid = (l+r) // 2
            if mid**2 <=x:
                ans = mid
                l = mid+1
            else:
                r = mid-1
        return ans


# @lc code=end

