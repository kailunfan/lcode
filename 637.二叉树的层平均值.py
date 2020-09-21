#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#
# https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/description/
#
# algorithms
# Easy (65.01%)
# Likes:    160
# Dislikes: 0
# Total Accepted:    25.5K
# Total Submissions: 39.1K
# Testcase Example:  '[3,9,20,15,7]'
#
# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。
# 
# 
# 
# 示例 1：
# 
# 输入：
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 输出：[3, 14.5, 11]
# 解释：
# 第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 节点值的范围在32位有符号整数范围内。
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        ans = []
        layer = [root]
        while layer:
            tmp = []
            s = 0
            for node in layer:
                s += node.val
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            ans.append(s/len(layer))
            layer = tmp
        return ans
        
        
# @lc code=end

