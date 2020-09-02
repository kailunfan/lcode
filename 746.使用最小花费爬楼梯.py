#
# @lc app=leetcode.cn id=746 lang=python
#
# [746] 使用最小花费爬楼梯
#
# https://leetcode-cn.com/problems/min-cost-climbing-stairs/description/
#
# algorithms
# Easy (48.09%)
# Likes:    297
# Dislikes: 0
# Total Accepted:    33.8K
# Total Submissions: 69.3K
# Testcase Example:  '[0,0,0,0]'
#
# 数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
#
# 每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
#
# 您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。
#
# 示例 1:
#
# 输入: cost = [10, 15, 20]
# 输出: 15
# 解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
#
#
# 示例 2:
#
# 输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出: 6
# 解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
#
#
# 注意：
#
#
# cost 的长度将会在 [2, 1000]。
# 每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。
#
#
#

# @lc code=start


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        status = {}
        # 用/不用
        status[0] = (cost[0],0) 
        status[1] = (cost[1],status[0])
        for i in range(2,len(cost)):
            use = cost[i] + min(status[i-1][0],status[i-1][1],status[i-2][0])
            not_use = status[i-1][0]
            status[i] = (use,not_use)
        return min(status[len(cost)-1][0],status[len(cost)-1][1])


# @lc code=end
