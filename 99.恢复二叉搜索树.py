#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#
# https://leetcode-cn.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Hard (56.30%)
# Likes:    208
# Dislikes: 0
# Total Accepted:    17.6K
# Total Submissions: 30.9K
# Testcase Example:  '[1,3,null,null,2]'
#
# 二叉搜索树中的两个节点被错误地交换。
# 
# 请在不改变其结构的情况下，恢复这棵树。
# 
# 示例 1:
# 
# 输入: [1,3,null,null,2]
# 
# 1
# /
# 3
# \
# 2
# 
# 输出: [3,1,null,null,2]
# 
# 3
# /
# 1
# \
# 2
# 
# 
# 示例 2:
# 
# 输入: [3,1,4,null,null,2]
# 
# ⁠ 3
# ⁠/ \
# 1   4
# /
# 2
# 
# 输出: [2,1,4,null,null,3]
# 
# ⁠ 2
# ⁠/ \
# 1   4
# /
# ⁠ 3
# 
# 进阶:
# 
# 
# 使用 O(n) 空间复杂度的解法很容易实现。
# 你能想出一个只使用常数空间的解决方案吗？
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 有序数组交换两个节点后有何特点?
        # 中序遍历
        pre_node = None
        swapped_nodes = []
        stack = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                # 处理
                if pre_node and cur.val < pre_node.val:
                    swapped_nodes.append((pre_node,cur))
                pre_node = cur
                cur = cur.right
        if len(swapped_nodes) == 1:
            swapped_nodes[0][0].val,swapped_nodes[0][1].val = swapped_nodes[0][1].val,swapped_nodes[0][0].val
        if len(swapped_nodes) == 2:
            swapped_nodes[0][0].val,swapped_nodes[1][1].val = swapped_nodes[1][1].val,swapped_nodes[0][0].val
# @lc code=end

