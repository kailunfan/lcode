#
# @lc app=leetcode.cn id=264 lang=python
#
# [264] 丑数 II
#
# https://leetcode-cn.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (51.20%)
# Likes:    296
# Dislikes: 0
# Total Accepted:    26.6K
# Total Submissions: 51K
# Testcase Example:  '10'
#
# 编写一个程序，找出第 n 个丑数。
#
# 丑数就是质因数只包含 2, 3, 5 的正整数。
#
# 示例:
#
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
#
# 说明:  
#
#
# 1 是丑数。
# n 不超过1690。
#
#
#

# @lc code=start


class Solution(object):
    nums = []

    def store(self):
        nums = [1]
        c2 = c3 = c5 = 0
        for i in range(1, 1690):
            new = min(nums[c2]*2, nums[c3]*3, nums[c5]*5)
            nums.append(new)
            if new == nums[c2]*2:
                c2 += 1
            if new == nums[c3]*3:
                c3 += 1
            if new == nums[c5]*5:
                c5 += 1
        self.nums = nums

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not self.nums:
            self.store()
        return self.nums[n-1]

# @lc code=end
print(Solution().store())