#
# @lc app=leetcode.cn id=222 lang=python
#
# [222] 完全二叉树的节点个数
#
# https://leetcode-cn.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (68.30%)
# Likes:    159
# Dislikes: 0
# Total Accepted:    21.3K
# Total Submissions: 30.7K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# 给出一个完全二叉树，求出该树的节点个数。
# 
# 说明：
# 
# 
# 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第
# h 层，则该层包含 1~ 2^h 个节点。
# 
# 示例:
# 
# 输入: 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠/ \  /
# 4  5 6
# 
# 输出: 6
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

    def compute_depth(self, node: TreeNode) -> int:
        """
        Return tree depth in O(d) time.
        """
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(self, idx: int, d: int, node: TreeNode) -> bool:
        """
        Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        Return True if last level node idx exists. 
        Binary search with O(d) complexity.
        """
        left, right = 0, 2**d - 1
        for _ in range(d):
            pivot = (left + right) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None
        
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        d = self.compute_depth(root)
        if d == 0:
            return 1
        
        # Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        # Perform binary search to check how many nodes exist.
        left, right = 1, 2**d - 1
        while left <= right:
            pivot = (left + right) // 2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1
        
        # The tree contains 2**d - 1 nodes on the first (d - 1) levels
        # and left nodes on the last level.
        return (2**d - 1) + left

# @lc code=end

