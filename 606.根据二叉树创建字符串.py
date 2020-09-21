#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#
# https://leetcode-cn.com/problems/construct-string-from-binary-tree/description/
#
# algorithms
# Easy (54.44%)
# Likes:    143
# Dislikes: 0
# Total Accepted:    15.7K
# Total Submissions: 28.7K
# Testcase Example:  '[1,2,3,4]'
#
# 你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。
#
# 空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。
#
# 示例 1:
#
#
# 输入: 二叉树: [1,2,3,4]
# ⁠      1
# ⁠    /   \
# ⁠   2     3
# ⁠  /
# ⁠ 4
#
# 输出: "1(2(4))(3)"
#
# 解释: 原本将是“1(2(4)())(3())”，
# 在你省略所有不必要的空括号对之后，
# 它将是“1(2(4))(3)”。
#
#
# 示例 2:
#
#
# 输入: 二叉树: [1,2,3,null,4]
# ⁠      1
# ⁠    /   \
# ⁠   2     3
# ⁠    \
# ⁠     4
#
# 输出: "1(2()(4))(3)"
#
# 解释: 和第一个示例相似，
# 除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。
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
    def tree2str(self, t: TreeNode) -> str:
        # 迭代
        if t == None:
            return ""
        stack = [t]
        output = []
        while stack:
            item = stack.pop()
            if item in [')', '(', '()']:
                output.append(item)
            else:
                node = item
                output.append(str(node.val))
                if node.right:
                    stack.extend((')',node.right,'('))
                    if not node.left:
                        stack.append('()')
                if node.left:
                    stack.extend((')',node.left,'('))
        return ''.join(output)

        # 递归
        def build(node):
            if not node:
                return ''
            l = build(node.left)
            r = build(node.right)
            ans = f'{node.val}'
            ans += f'({l})' if l or r else ''
            ans += f'({r})' if r else ''
            return ans
        return build(t)


# @lc code=end
