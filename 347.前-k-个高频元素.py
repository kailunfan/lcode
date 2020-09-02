#
# @lc app=leetcode.cn id=347 lang=python
#
# [347] 前 K 个高频元素
#
# https://leetcode-cn.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (61.09%)
# Likes:    357
# Dislikes: 0
# Total Accepted:    58.3K
# Total Submissions: 96.1K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
#
#
#
# 示例 1:
#
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#
#
# 示例 2:
#
# 输入: nums = [1], k = 1
# 输出: [1]
#
#
#
# 提示：
#
#
# 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
# 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
# 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
# 你可以按任意顺序返回答案。
#
#
#

# @lc code=start

from collections import Counter
import heapq


class Solution(object):
    def topKFrequent(self, nums, kn):
        counts = Counter(nums)
        counts = [(k, v) for k, v in counts.items()]
        ans = heapq.nlargest(kn, counts, key=lambda x: x[1])
        return [x[0] for x in ans]

    # def topKFrequent(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: List[int]
    #     """
    #     # 维护一个小顶堆,插入元素,堆化
    #     i = 0
    #     h = []
    #     for key, value in Counter(nums).items():
    #         if i < k:
    #             i += 1
    #             h.insert(0, [key, value])
    #             self.heapfy_top(h)
    #             continue
    #         if value < h[0][1]:
    #             continue
    #         h[0] = [key, value]
    #         self.heapfy_top(h)
    #     return [x[0] for x in h]

    # def heapfy_top(self, h):
    #     c = 0
    #     l = len(h)
    #     while True:
    #         lc = 2*c + 1
    #         rc = 2*c + 2
    #         if lc >= l:
    #             break
    #         tc = lc
    #         if rc < l and h[lc][1] > h[rc][1]:
    #             tc = rc
    #         if h[c][1] <= h[tc][1]:
    #             break
    #         h[c], h[tc] = h[tc], h[c]
    #         c = tc
# @lc code=end
