#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# https://leetcode.cn/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (52.24%)
# Likes:    2045
# Dislikes: 0
# Total Accepted:    606.4K
# Total Submissions: 1.2M
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
#
#
# 示例 1：
#
#
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
#
# 示例 2：
#
#
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
#
#
#
#
# 提示：
#
#
# 0
# -10^9
#
#
#

# @lc code=start
from typing import List


class Solution:
    def longestConsecutive1(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        cur = 1
        l = len(nums)

        ans = 0
        this_ans = 1
        while cur < l:
            if nums[cur]-nums[cur-1] == 1:
                this_ans += 1
                ans = max(this_ans, ans)
            else:
                this_ans = 1
            cur = cur+1

        ans = max(this_ans, ans)
        return ans

    def longestConsecutive2(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        ans = 0
        m = {i: -1 for i in nums}
        for i in nums:
            v = m.get(i)
            if v != -1:
                continue

            this_ans = 0
            cur = i
            while cur+1 in m:
                if m[cur+1] != -1:
                    this_ans = m[cur+1]
                    break
                cur = cur+1

            while cur >= i:
                this_ans += 1
                m[cur] = this_ans
                ans = max(ans, this_ans)
                cur -= 1

        return ans

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        m = {i: 0 for i in nums}

        def search(i):
            if m[i] != 0:
                return m[i]
            if i+1 in m:
                ans = search(i+1)+1
            else:
                ans = 1
            m[i] = ans
            return ans
        return max(search(i) for i in nums)


# @lc code=end
