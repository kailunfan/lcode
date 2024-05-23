#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# https://leetcode-cn.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (59.15%)
# Likes:    225
# Dislikes: 0
# Total Accepted:    48.5K
# Total Submissions: 81.4K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \    / \
# ⁠       7    2  5   1
#         \
#          0
#
# 返回:
#
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
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
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []

        # 深度优先遍历(前序)
        stack = [(root, [root.val])]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                if sum(path) == s:
                    ans.append(path)
                continue
            if node.right:
                stack.append((node.right, path+[node.right.val]))
            if node.left:
                stack.append((node.left, path+[node.left.val]))
        return ans

        # 广度优先遍历
        q = [(root, [root.val])]
        while q:
            node, path = q.pop(0)
            if not node.left and not node.right:
                if sum(path) == s:
                    ans.append(path)
                continue
            if node.left:
                q.append((node.left, path+[node.left.val]))
            if node.right:
                q.append((node.right, path+[node.right.val]))
        return ans

        # def check(node,path):
        #     if not any([node.left,node.right]) and self.total(path) == sum:
        #         res.append(path)
        #         return
        #     if node.left:
        #         check(node.left,path+[node.left.val])
        #     if node.right:
        #         check(node.right,path+[node.right.val])
        # check(root,[root.val])
        # return res

    # def total(self, li):
    #     return sum(li)

# @lc code=end
