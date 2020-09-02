#
# @lc app=leetcode.cn id=215 lang=python
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (62.03%)
# Likes:    500
# Dislikes: 0
# Total Accepted:    125.3K
# Total Submissions: 200.2K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#
#
# 示例 2:
#
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
#
# 说明:
#
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
#
#

# @lc code=start
import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = []
        for i, num in enumerate(nums):
            if i < k:
                h.insert(0, num)
                self.heapfy_top(h)
                continue
            if num <= h[0]:
                continue
            # 弹出堆顶元素,从堆顶插入新元素
            h[0] = num
            self.heapfy_top(h)
        return h[0]

    def heapfy_top(self, h):
        c = 0
        while True:
            lc = 2 * c + 1
            rc = 2 * c + 2
            if lc >= len(h):
                break
            tc = lc  # target cur
            if rc < len(h) and h[lc] > h[rc]:
                tc = rc
            if h[c] <= h[tc]:
                break
            h[c], h[tc] = h[tc], h[c]
            c = tc


# @lc code=end
