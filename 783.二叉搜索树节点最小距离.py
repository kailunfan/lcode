#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#
# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/description/
#
# algorithms
# Easy (53.53%)
# Likes:    72
# Dislikes: 0
# Total Accepted:    16.3K
# Total Submissions: 30.3K
# Testcase Example:  '[4,2,6,1,3,null,null]'
#
# 给定一个二叉搜索树的根节点 root，返回树中任意两节点的差的最小值。
# 
# 
# 
# 示例：
# 
# 输入: root = [4,2,6,1,3,null,null]
# 输出: 1
# 解释:
# 注意，root是树节点对象(TreeNode object)，而不是数组。
# 
# 给定的树 [4,2,6,1,3,null,null] 可表示为下图:
# 
# ⁠         4
# ⁠       /   \
# ⁠     2      6
# ⁠    / \    
# ⁠   1   3  
# 
# 最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。
# 
# 
# 
# 注意：
# 
# 
# 二叉树的大小范围在 2 到 100。
# 二叉树总是有效的，每个节点的值都是整数，且不重复。
# 本题与 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
# 相同
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
    def minDiffInBST(self, root: TreeNode) -> int:
        # 中序遍历
        ans = float('inf')
        pre = float('-inf')
        stack = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                ans = min(ans,cur.val - pre)
                pre = cur.val
                cur = cur.right
        return ans
# @lc code=end

