#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
# https://leetcode-cn.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (63.50%)
# Likes:    262
# Dislikes: 0
# Total Accepted:    37.5K
# Total Submissions: 58.7K
# Testcase Example:  '[1,2,3,null,5]'
#
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
#
# 输入:
#
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
#
# 输出: ["1->2->5", "1->3"]
#
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
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
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        ans = []
        # 回溯
        # def search(node, prefix):
        #     if not node.left and not node.right:
        #         ans.append(prefix)
        #         return
        #     if node.left:
        #         search(node.left, "{}->{}".format(prefix, node.left.val))
        #     if node.right:
        #         search(node.right, "{}->{}".format(prefix, node.right.val))

        # search(root, '{}'.format(root.val))
        # return ans

        # 迭代3
        q = [(root, f"{root.val}")]
        while q:
            node,value = q.pop(0)
            if not node.left and not node.right:
                ans.append(value)
                continue
            if node.left:
                q.append((node.left,f"{value}->{node.left.val}"))
            if node.right:
                q.append((node.right,f"{value}->{node.right.val}"))
        return ans

        # 迭代2
        stack = [(root, f"{root.val}")]
        while stack:
            node, value = stack.pop()
            if not node.left and not node.right:
                ans.append(value)
            if node.left:
                stack.append((node.left,f"{value}->{node.left.val}"))
            if node.right:
                stack.append((node.right,f"{value}->{node.right.val}"))
        return ans

        # 迭代
        visited = set([root])
        stack = [root]
        cur = root
        while stack or cur:
            if cur.left and not cur.left in visited:
                stack.append(cur.left)
                cur = cur.left
                visited.add(cur)
            elif cur.right and not cur.right in visited:
                stack.append(cur.right)
                cur = cur.right
                visited.add(cur)
            else:
                # 子节点
                if not cur.left and not cur.right:
                    value = [str(v.val) for v in stack]
                    ans.append('->'.join(value))
                if stack:
                    stack.pop()
                if stack:
                    cur = stack[-1]
                else:
                    cur = None

        return ans


# @lc code=end
