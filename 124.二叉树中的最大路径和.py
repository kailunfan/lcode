#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (39.93%)
# Likes:    429
# Dislikes: 0
# Total Accepted:    39.1K
# Total Submissions: 96.8K
# Testcase Example:  '[1,2,3]'
#
# 给定一个非空二叉树，返回其最大路径和。
#
# 本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
#
# 示例 1:
#
# 输入: [1,2,3]
#
# ⁠      1
# ⁠     / \
# ⁠    2   3
#
# 输出: 6
#
#
# 示例 2:
#
# 输入: [-10,9,20,null,null,15,7]
#
# -10
# / \
# 9  20
# /  \
# 15   7
#
# 输出: 42
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

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 迭代
        # ans = float('-inf')
        # stack = [(root,max(root.val,0))]
        # while stack:
        #     node,res = stack.pop()
        #     ans = max(ans,res)
        #     if node.left:
        #         stack.append((node.left,max(res,0)+node.left.val))
        #     if node.right:
        #         stack.append((node.right,max(res,0)+node.right.val))
        # return ans
            
            
        # 递归
        max_res = float('-inf')
        def search(node):
            if not node:
                return 0
            nonlocal max_res
            left = search(node.left)
            right = search(node.right)
            # 以node为根
            res = node.val
            res += max(0, left)
            res += max(0, right)
            max_res = max(max_res,res)
            # node为路径上一个点
            return node.val + max(0,left,right)
        
        search(root)
        return max_res

# @lc code=end
