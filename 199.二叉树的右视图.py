#
# @lc app=leetcode.cn id=199 lang=python
#
# [199] 二叉树的右视图
#
# https://leetcode-cn.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (64.10%)
# Likes:    233
# Dislikes: 0
# Total Accepted:    46.4K
# Total Submissions: 72.9K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
# 
# 示例:
# 
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 中-右-左 遍历,只储存每层第一个值
        if not root:
            return []
        res = {}
        stack = [(root,0)]
        while stack:
            node,depth = stack.pop()
            if not res.get(depth):
                res[depth] = node.val
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return list(res.values())

        # 层次遍历的变种
        stack,res  = [root],[]
        while stack:
            tmp = None
            tmp_stack = []
            for node in stack:
                if node:
                    tmp = node.val
                    tmp_stack.append(node.left)
                    tmp_stack.append(node.right)
            stack = tmp_stack  
            if tmp: 
                res.append(tmp)
        return res
                

# @lc code=end

