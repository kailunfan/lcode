#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#
# https://leetcode-cn.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (53.62%)
# Likes:    146
# Dislikes: 0
# Total Accepted:    10.8K
# Total Submissions: 20K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# 给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
#
# 两棵树重复是指它们具有相同的结构以及相同的结点值。
#
# 示例 1：
#
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   2   4
# ⁠      /
# ⁠     4
#
#
# 下面是两个重复的子树：
#
# ⁠     2
# ⁠    /
# ⁠   4
#
#
# 和
#
# ⁠   4
#
#
# 因此，你需要以列表的形式返回上述重复子树的根结点。
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
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        # 关键点,序列化
        ans = []
        ansed = set()
        visited = set()
        def search(node):
            if not node:
                return ''
            res = f'{node.val}({search(node.left)})({search(node.right)})'
            if res in visited and res not in ansed:
                ans.append(node)
                ansed.add(res)
            else:
                visited.add(res)
            return res

        search(root)
        return ans
# @lc code=end
