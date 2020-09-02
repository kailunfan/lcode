#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#
# https://leetcode-cn.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (48.50%)
# Likes:    295
# Dislikes: 0
# Total Accepted:    42.1K
# Total Submissions: 85.9K
# Testcase Example:  '3\n3'
#
# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
# 
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# 给定 n 和 k，返回第 k 个排列。
# 
# 说明：
# 
# 
# 给定 n 的范围是 [1, 9]。
# 给定 k 的范围是[1,  n!]。
# 
# 
# 示例 1:
# 
# 输入: n = 3, k = 3
# 输出: "213"
# 
# 
# 示例 2:
# 
# 输入: n = 4, k = 9
# 输出: "2314"
# 
# 
#

# @lc code=start
import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 转换为从0开始
        # k = k - 1
        # ans = []
        # def calc(sn,options):
        #     if len(ans) == n:
        #         return
        #     one_time_num = math.factorial(len(options)-1)
        #     times,remain = divmod(sn,one_time_num)
        #     ind = times
        #     ans.append(options[ind])
        #     options.remove(options[ind])
        #     calc(remain,options)
        
        # calc(k,[str(i+1) for i in range(n)])
        # return ''.join(ans)
        
        # 迭代
        k = k - 1
        ans = ''
        options = [str(i+1) for i in range(n)]

        # 每一个循环都是计算剩余元素的第一位值
        while len(ans) < n:
            one_time_num = math.factorial(len(options)-1)
            times,remain = divmod(k,one_time_num)
            ind = times
            ans += options[ind]
            options.remove(options[ind])
            k = remain
        return ans


        
# @lc code=end

