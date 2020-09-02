#
# @lc app=leetcode.cn id=449 lang=python
#
# [449] 序列化和反序列化二叉搜索树
#
# https://leetcode-cn.com/problems/serialize-and-deserialize-bst/description/
#
# algorithms
# Medium (51.36%)
# Likes:    71
# Dislikes: 0
# Total Accepted:    5.4K
# Total Submissions: 10.3K
# Testcase Example:  '[2,1,3]'
#
# 序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。
#
# 设计一个算法来序列化和反序列化二叉搜索树。 对序列化/反序列化算法的工作方式没有限制。
# 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。
#
# 编码的字符串应尽可能紧凑。
#
# 注意：不要使用类成员/全局/静态变量来存储状态。 你的序列化和反序列化算法应该是无状态的。
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import json


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # 前序遍历
        res, stack = [], []
        cur = root
        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                cur = cur.right
        return json.dumps(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # 通过前序遍历和中序遍历结果还原树
        prev_order = json.loads(data)

        def build(list):
            if not list:
                return None
            node = TreeNode(list[0])
            node.left = build([i for i in list[1:] if i <= list[0]])
            node.right = build([i for i in list[1:] if i > list[0]])
            return node
        return build(prev_order)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.
# deserialize(codec.serialize(root))
# @lc code=end
