#
# @lc app=leetcode.cn id=100 lang=python
#
# [100] 相同的树
#
# https://leetcode-cn.com/problems/same-tree/description/
#
# algorithms
# Easy (57.17%)
# Likes:    364
# Dislikes: 0
# Total Accepted:    87.8K
# Total Submissions: 152.4K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# 给定两个二叉树，编写一个函数来检验它们是否相同。
# 
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
# 
# 示例 1:
# 
# 输入:       1         1
# ⁠         / \       / \
# ⁠        2   3     2   3
# 
# ⁠       [1,2,3],   [1,2,3]
# 
# 输出: true
# 
# 示例 2:
# 
# 输入:      1          1
# ⁠         /           \
# ⁠        2             2
# 
# ⁠       [1,2],     [1,null,2]
# 
# 输出: false
# 
# 
# 示例 3:
# 
# 输入:       1         1
# ⁠         / \       / \
# ⁠        2   1     1   2
# 
# ⁠       [1,2,1],   [1,1,2]
# 
# 输出: false
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
    def isSameTree(slef, p, q):
        # 标准解法
        queue = [(p,q)]
        while queue:
            l,r = queue.pop(0)
            if not any([l,r]):
                continue
            if not all([l,r]):
                return False
            if l.val != r.val:
                return False
            if l and r:
                queue.append((l.left,r.left))
                queue.append((l.right,r.right))
        return True


    def isSameTree1(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # left_stack = []
        # right_stack = []
        # lc,rc = p, q
        # while (lc or left_stack) or (rc or right_stack):
        #     lv = rv = None
        #     if (lc or left_stack):
        #         if lc:
        #             lv = lc.val
        #             left_stack.append(lc)
        #             lc = lc.left
        #         else:
        #             lp = left_stack.pop()
        #             lc = lp.right
        #     if (rc or right_stack):      
        #         if rc:
        #             rv = rc.val
        #             right_stack.append(rc)
        #             rc = rc.left
        #         else:
        #             lp = right_stack.pop()
        #             rc = lp.right
        #     if (lv is not None or rv is not None) and (lv != rv):
        #         return False

        # return True

        ## 生成器
        pt = self.tree_gen(p)
        qt = self.tree_gen(q)
        prun = qrun = True
        while prun or qrun:
            try:
                pv = pt.next()
            except StopIteration:
                pv = None
                prun = False
            try:
                qv = qt.next()
            except StopIteration:
                qv = None
                qrun = False
            if (pv is not None or qv is not None) and (pv != qv):
                return False
        return True

    def tree_gen(self, root):
        # 广度遍历
        stack = [root]
        while stack:
            tmp = []
            for i in stack:
                yield (i.val if i else None)
                if i:
                    tmp.append(i.left)
                    tmp.append(i.right)
            stack = tmp               

    
# @lc code=end

