#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#
# https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/description/
#
# algorithms
# Easy (56.18%)
# Likes:    172
# Dislikes: 0
# Total Accepted:    20.9K
# Total Submissions: 36.9K
# Testcase Example:  '[5,3,6,2,4,null,7]\n9'
#
# 给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
#
# 案例 1:
#
#
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
#
# Target = 9
#
# 输出: True
#
#
#
#
# 案例 2:
#
#
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
#
# Target = 28
#
# 输出: False
#
#
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


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        # 中序遍历+查找
        stack, lst = [], []
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                lst.append(cur.val)
                cur = cur.right
        # 查找
        lc = 0
        rc = len(lst) - 1
        while lc < rc:
            s = lst[lc] + lst[rc]
            if s == k:
                return True
            if s < k:
                lc += 1
            else:
                rc -= 1
        return False


# @lc code=end
