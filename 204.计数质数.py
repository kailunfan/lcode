#
# @lc app=leetcode.cn id=204 lang=python
#
# [204] 计数质数
#
# https://leetcode-cn.com/problems/count-primes/description/
#
# algorithms
# Easy (33.32%)
# Likes:    368
# Dislikes: 0
# Total Accepted:    62.1K
# Total Submissions: 182.2K
# Testcase Example:  '10'
#
# 统计所有小于非负整数 n 的质数的数量。
#
# 示例:
#
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
#
#
#

# @lc code=start


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 厄拉多塞筛法
        # 全部初始化为质数
        state = [1 for _ in range(n)]
        # 将质数的奇数倍设为非质数
        for i in range(2,n**0.5+1):
            if state[i]:
                


        
# @lc code=end
