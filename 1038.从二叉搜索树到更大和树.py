#
# @lc app=leetcode.cn id=1038 lang=python
#
# [1038] 从二叉搜索树到更大和树
#
# https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/description/
#
# algorithms
# Medium (73.75%)
# Likes:    52
# Dislikes: 0
# Total Accepted:    9.1K
# Total Submissions: 12.1K
# Testcase Example:  '[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'
#
# 给出二叉 搜索 树的根节点，该二叉树的节点值各不相同，修改二叉树，使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
# 
# 提醒一下，二叉搜索树满足下列约束条件：
# 
# 
# 节点的左子树仅包含键 小于 节点键的节点。
# 节点的右子树仅包含键 大于 节点键的节点。
# 左右子树也必须是二叉搜索树。
# 
# 
# 
# 
# 示例：
# 
# 
# 
# 输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# 输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中的节点数介于 1 和 100 之间。
# 每个节点的值介于 0 和 100 之间。
# 给定的树为二叉搜索树。
# 
# 
# 
# 
# 注意：该题目与 538: https://leetcode-cn.com/problems/convert-bst-to-greater-tree/
# 相同
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
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 中序遍历变种, 右->中->左
        if not root:
            return root
        cur = root
        stack = []
        add_target = 0
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur.val += add_target
                add_target = cur.val
                cur = cur.left
        return root

# @lc code=end

