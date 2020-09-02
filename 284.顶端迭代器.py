#
# @lc app=leetcode.cn id=284 lang=python3
#
# [284] 顶端迭代器
#
# https://leetcode-cn.com/problems/peeking-iterator/description/
#
# algorithms
# Medium (71.47%)
# Likes:    49
# Dislikes: 0
# Total Accepted:    4.5K
# Total Submissions: 6.3K
# Testcase Example:  '["PeekingIterator","next","peek","next","next","hasNext"]\n' +
  '[[[1,2,3]],[],[],[],[],[]]'
#
# 给定一个迭代器类的接口，接口包含两个方法： next() 和 hasNext()。设计并实现一个支持 peek() 操作的顶端迭代器 --
# 其本质就是把原本应由 next() 方法返回的元素 peek() 出来。
# 
# 示例:
# 
# 假设迭代器被初始化为列表 [1,2,3]。
# 
# 调用 next() 返回 1，得到列表中的第一个元素。
# 现在调用 peek() 返回 2，下一个元素。在此之后调用 next() 仍然返回 2。
# 最后一次调用 next() 返回 3，末尾元素。在此之后调用 hasNext() 应该返回 false。
# 
# 
# 进阶：你将如何拓展你的设计？使之变得通用化，从而适应所有的类型，而不只是整数型？
# 
#

# @lc code=start
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peeked = False
        self.peek_val = None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peeked:
            self.peeked = True
            self.peek_val = self.iterator.next()
        return self.peek_val
        

    def next(self):
        """
        :rtype: int
        """
        if self.peeked:
            self.peeked = False
            return self.peek_val
        return self.iterator.next()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peeked:
            return True
        return self.iterator.hasNext()
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
# @lc code=end

