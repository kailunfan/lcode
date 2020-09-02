#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
# https://leetcode-cn.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (44.78%)
# Likes:    203
# Dislikes: 0
# Total Accepted:    17.6K
# Total Submissions: 37.8K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' +
'[[],[1],[2],[],[3],[]]'
#
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
#
# 例如，
#
# [2,3,4] 的中位数是 3
#
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
#
# 设计一个支持以下两种操作的数据结构：
#
#
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。
#
#
# 示例：
#
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2
#
# 进阶:
#
#
# 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
# 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
#
#
#

# @lc code=start

import bisect

from heapq import heappop, heappush, heappushpop


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.content = []
        self.max_heap, self.min_heap = [], []

    def addNum(self, num: int) -> None:
        # 直接索索插入位置,超时
        # if num is None:
        #     return
        # if not self.content:
        #     self.content.append(num)
        #     return
        # cur = len(self.content) - 1
        # while cur >= 0 and self.content[cur] > num:
        #     cur -= 1
        # self.content.insert(cur+1, num)

        # 二分查找插入位置,依然超时
        # bisect.insort_right(self.content, num)

        # 维护两个堆,一个大顶堆,维护前半部分元素,一个小顶堆维护后半部分元素.
        if len(self.max_heap) == len(self.min_heap):
            # 小顶堆加元素
            heappush(self.min_heap, -heappushpop(self.max_heap, -num))
        else:
            heappush(self.max_heap, -heappushpop(self.min_heap, num))

    def findMedian(self) -> float:
        # le = len(self.content)
        # print(le, self.content)
        # if le % 2 == 1:
        #     cur = le // 2
        #     return self.content[cur]
        # c1 = le // 2
        # c2 = c1 - 1
        # return (self.content[c1] + self.content[c2]) / 2
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        return self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
