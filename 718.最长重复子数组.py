#
# @lc app=leetcode.cn id=718 lang=python
#
# [718] 最长重复子数组
#
# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (49.73%)
# Likes:    182
# Dislikes: 0
# Total Accepted:    13.3K
# Total Submissions: 26.3K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
#
# 示例 1:
#
#
# 输入:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出: 3
# 解释:
# 长度最长的公共子数组是 [3, 2, 1]。
#
#
# 说明:
#
#
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
#
#
#

# @lc code=start


class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # 动态规划
        # 关键点,状态表和状态转义方程
        # 状态表: 以i结尾的A和以j结尾的B的公共子数组的长度.
        # 状态转移方程: 左上角加1
        
        dp = [[0 for _ in range(len(A))] for _ in range(len(B))]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = 1
        return max([max(row) for row in dp])


# a = [1,2,3,2,1]
# b = [3,2,1,4,7]
# Solution().findLength(a,b)

# @lc code=end
