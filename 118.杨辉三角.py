#
# @lc app=leetcode.cn id=118 lang=python
#
# [118] 杨辉三角
#
# https://leetcode-cn.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (66.19%)
# Likes:    313
# Dislikes: 0
# Total Accepted:    84.8K
# Total Submissions: 127.3K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 5
# 输出:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
#
#

# @lc code=start


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        layer = [1]
        ans = []
        for i in range(numRows):
            ans.append(layer)
            new_layer = [1]
            for i in range(len(layer)-1):
                new_layer.append(layer[i]+layer[i+1])
            new_layer.append(1)
            layer = new_layer
        return ans

# @lc code=end

# Solution().generate(5)