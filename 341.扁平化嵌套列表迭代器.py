#
# @lc app=leetcode.cn id=341 lang=python
#
# [341] 扁平化嵌套列表迭代器
#
# https://leetcode-cn.com/problems/flatten-nested-list-iterator/description/
#
# algorithms
# Medium (63.04%)
# Likes:    113
# Dislikes: 0
# Total Accepted:    8.8K
# Total Submissions: 13.9K
# Testcase Example:  '[[1,1],2,[1,1]]'
#
# 给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
#
# 列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。
#
#
#
# 示例 1:
#
# 输入: [[1,1],2,[1,1]]
# 输出: [1,1,2,1,1]
# 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
#
# 示例 2:
#
# 输入: [1,[4,[6]]]
# 输出: [1,4,6]
# 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。
#
#
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.next_val = None

        def iterator(nestedList):
            for i in nestedList:
                if i.isInteger():
                    yield i.getInteger()
                else:
                    # yield from iterator(i.getList())
                    for j in iterator(i.getList()):
                        yield j             

        self.itor = iterator(nestedList)
                

    def next(self):
        """
        :rtype: int
        """
        return self.next_val
            
    def hasNext(self):
        """
        :rtype: bool
        """
        try:
            self.next_val = next(self.itor)
            return True
        except StopIteration:
            return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end



