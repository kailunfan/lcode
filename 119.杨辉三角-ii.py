#
# @lc app=leetcode.cn id=119 lang=python
#
# [119] 杨辉三角 II
#
# https://leetcode-cn.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (60.76%)
# Likes:    156
# Dislikes: 0
# Total Accepted:    56.1K
# Total Submissions: 91.7K
# Testcase Example:  '3'
#
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 3
# 输出: [1,3,3,1]
# 
# 
# 进阶：
# 
# 你可以优化你的算法到 O(k) 空间复杂度吗？
# 
#

# @lc code=start
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        k = rowIndex
        factorials = [1]
        for i in range(1,k+1):
            factorials.append(i*factorials[i-1])
        ans = []
        # for i in range(k+1):
        #     this_ans = factorials[k] / (factorials[i] * factorials[k-i])
        #     ans.append(this_ans)
        # return ans

        for i in range(k//2+1):
            this_ans = factorials[k] / (factorials[i] * factorials[k-i])
            ans.append(this_ans)
        for i in range(k//2+1,k+1):
            ans.append(ans[k-i])
        return ans            

# @lc code=end

