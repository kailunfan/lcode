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
        # BST中序遍历为升序数组
        if not root:
            return []
        ans = []

        max_count = 0
        count = 0
        prev_val = None
        cur_val = None
        

        # 中序遍历
        stack = []
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                
                # 逻辑start
                cur_val = cur.val
                if cur_val == prev_val:
                    count += 1
                else:
                    if count == max_count:
                        ans.append(prev_val)
                    elif count > max_count:
                        ans = [prev_val]
                        max_count = count
                    
                    prev_val = cur_val
                    count = 1
                # 逻辑end

                cur = cur.right

        if count > max_count:
            ans = [cur_val]
        elif count == max_count:
            ans.append(cur_val)
        return [i for i in ans if i is not None]


# @lc code=end
