#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Medium (47.04%)
# Likes:    714
# Dislikes: 0
# Total Accepted:    74.8K
# Total Submissions: 150.7K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
'[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
#
# 获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) -
# 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
#
#
#
# 进阶:
#
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？
#
#
#
# 示例:
#
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得关键字 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得关键字 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
#
#
#

# @lc code=start
from collections import OrderedDict


# class LRUCache(OrderedDict):

#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         super().__init__()
#         self.capacity = capacity

#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         if key not in self:
#             return -1
#         self.move_to_end(key)
#         return self[key]

#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
#         if key in self:
#             self.move_to_end(key)
#         self[key] = value
#         if len(self) > self.capacity:
#             self.popitem(last=False)


class Node:
    def __init__(self, val, key=None):
        self.val = val
        self.next = None
        self.pre = None
        self.key = key


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head, self.tail = Node(None), Node(Node)
        self.head.next, self.tail.pre = self.tail, self.head
        self.map = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1
        node = self.map[key]
        self.move_to_end(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # 存在,修改节点val和位置
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.move_to_end(node)
            return
        # 不存在,在最后添加节点
        node = Node(value, key)
        self.map[key] = node
        self.append(node)
        # 容量
        if len(self.map) > self.capacity:
            self.pop_head()

    def move_to_end(self, node):
        node.next.pre, node.pre.next = node.pre, node.next
        self.tail.pre.next, self.tail.pre, node.pre, node.next = node, node, self.tail.pre, self.tail

    def pop_head(self):
        node = self.head.next
        self.head.next, self.head.next.next.pre = self.head.next.next, self.head
        del self.map[node.key]

    def append(self, node):
        self.tail.pre.next, self.tail.pre, node.pre, node.next = node, node, self.tail.pre, self.tail


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
