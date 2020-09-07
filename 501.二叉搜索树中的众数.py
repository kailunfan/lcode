#
# @lc app=leetcode.cn id=501 lang=python
#
# [501] 二叉搜索树中的众数
#
# https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/description/
#
# algorithms
# Easy (44.34%)
# Likes:    105
# Dislikes: 0
# Total Accepted:    13.6K
# Total Submissions: 30.4K
# Testcase Example:  '[1,null,2,2]'
#
# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
#
# 假定 BST 有如下定义：
#
#
# 结点左子树中所含结点的值小于等于当前结点的值
# 结点右子树中所含结点的值大于等于当前结点的值
# 左子树和右子树都是二叉搜索树
#
#
# 例如：
# 给定 BST [1,null,2,2],
#
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  2
#
#
# 返回[2].
#
# 提示：如果众数超过1个，不需考虑输出顺序
#
# 进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
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
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # BST中序遍历
        # 遍历时可以求出每个数字出现的次数
        # 记录最大次数和众数集合,如果超过最大次数,则更新
        if not root:
            return []
        ans = []
        stack = []
        cur = root
        base_val = None
        
        max_count = 0
        this_count = 0
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                # 处理逻辑
                if cur.val == base_val:
                    this_count += 1
                else:
                    if base_val is not None:
                        if this_count > max_count:
                            ans = [base_val]
                            max_count = this_count
                        elif this_count == max_count:
                            ans.append(base_val)
                    this_count = 1
                    base_val = cur.val
                cur = cur.right

        if this_count > max_count:
            ans = [base_val]
        elif this_count == max_count:
            ans.append(base_val)

        return ans
    

# @lc code=end
