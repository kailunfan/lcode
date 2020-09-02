#
# @lc app=leetcode.cn id=260 lang=python
#
# [260] 只出现一次的数字 III
#
# https://leetcode-cn.com/problems/single-number-iii/description/
#
# algorithms
# Medium (71.30%)
# Likes:    233
# Dislikes: 0
# Total Accepted:    22.9K
# Total Submissions: 31.5K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
#
# 示例 :
#
# 输入: [1,2,1,3,2,5]
# 输出: [3,5]
#
# 注意：
#
#
# 结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
# 你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
#
#
#

# @lc code=start
from functools import reduce


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 先得到两个数的异或值
        xor = reduce(lambda x, y: x ^ y, nums)
        # 保留异或值最右边的1,其余全设为0
        diff = xor & -xor

        ans = 0
        for n in nums:
            if diff & n:
                ans ^= n
        return [ans, xor ^ ans]


# @lc code=end
