#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#
# https://leetcode-cn.com/problems/ones-and-zeroes/description/
#
# algorithms
# Medium (54.90%)
# Likes:    216
# Dislikes: 0
# Total Accepted:    17.3K
# Total Submissions: 31.3K
# Testcase Example:  '["10","0001","111001","1","0"]\n5\n3'
#
# 在计算机界中，我们总是追求用有限的资源获取最大的收益。
#
# 现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。
#
# 你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。
#
# 注意:
#
#
# 给定 0 和 1 的数量都不会超过 100。
# 给定字符串数组的长度不会超过 600。
#
#
# 示例 1:
#
#
# 输入: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
# 输出: 4
#
# 解释: 总共 4 个字符串可以通过 5 个 0 和 3 个 1 拼出，即 "10","0001","1","0" 。
#
#
# 示例 2:
#
#
# 输入: Array = {"10", "0", "1"}, m = 1, n = 1
# 输出: 2
#
# 解释: 你可以拼出 "10"，但之后就没有剩余数字了。更好的选择是拼出 "0" 和 "1" 。
#
#
#

# @lc code=start

from functools import lru_cache


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 动态规划
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for s in strs:
            zero_count = s.count('0')
            one_count = s.count('1')
            for i in range(n, one_count-1, -1):
                for j in range(m, zero_count-1, -1):
                    dp[i][j] = max(dp[i][j], 1+dp[i-one_count][j-zero_count])
        return dp[-1][-1]

        # 递归
        # 回溯,对每一个候选元素,做用与不用的判断

        @lru_cache(None)
        def search(ind, zero_num, one_num):
            if ind == len(strs):
                return 0
            zero_count = strs[ind].count('0')
            one_count = strs[ind].count('1')
            # 没选候选项
            res = search(ind+1, zero_num, one_num)
            # 选了这个候选项
            if zero_num >= zero_count and one_num >= one_count:
                res = max(res, 1 + search(ind+1, zero_num - zero_count, one_num-one_count))
            return res

        return search(0, m, n)


# @lc code=end
