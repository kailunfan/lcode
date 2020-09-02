#
# @lc app=leetcode.cn id=421 lang=python
#
# [421] 数组中两个数的最大异或值
#
# https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
#
# algorithms
# Medium (59.09%)
# Likes:    130
# Dislikes: 0
# Total Accepted:    4.6K
# Total Submissions: 7.9K
# Testcase Example:  '[3,10,5,25,2,8]'
#
# 给定一个非空数组，数组中元素为 a0, a1, a2, … , an-1，其中 0 ≤ ai < 2^31 。
#
# 找到 ai 和aj 最大的异或 (XOR) 运算结果，其中0 ≤ i,  j < n 。
#
# 你能在O(n)的时间解决这个问题吗？
#
# 示例:
#
#
# 输入: [3, 10, 5, 25, 2, 8]
#
# 输出: 28
#
# 解释: 最大的结果是 5 ^ 25 = 28.
#
#
#

# @lc code=start


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 补齐
        L = len(bin(max(nums))) - 2
        new_nums = []
        for num in nums:
            new_num = []
            for i in range(L):
                if num & (1 << (L-i-1)):
                    new_num.append(1)
                else:
                    new_num.append(0)
            new_nums.append(new_num)
        # 构造字典树
        max_xor = 0
        trie = {}
        for num in new_nums:
            node = trie
            xor_node = trie
            curr_xor = 0
            for bit in num:
                if not bit in node:
                    node[bit] = {}
                node = node[bit]
                
                toggled_bit = 1 - bit
                if toggled_bit in xor_node:
                    curr_xor = (curr_xor << 1) | 1
                    xor_node = xor_node[toggled_bit]
                else:
                    curr_xor = curr_xor << 1
                    xor_node = xor_node[bit]

            max_xor = max(max_xor, curr_xor)

        return max_xor

# @lc code=end
