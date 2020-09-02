#
# @lc app=leetcode.cn id=117 lang=python
#
# [117] 填充每个节点的下一个右侧节点指针 II
#
# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (47.30%)
# Likes:    143
# Dislikes: 0
# Total Accepted:    20.7K
# Total Submissions: 42.6K
# Testcase Example:  '[1,2,3,4,5,null,7]'
#
# 给定一个二叉树
# 
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
# 
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
# 
# 初始状态下，所有 next 指针都被设置为 NULL。
# 
# 
# 
# 进阶：
# 
# 
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
# 
# 
# 
# 
# 示例：
# 
# 
# 
# 输入：root = [1,2,3,4,5,null,7]
# 输出：[1,#,2,3,#,4,5,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
# 
# 
# 
# 提示：
# 
# 
# 树中的节点数小于 6000
# -100 <= node.val <= 100
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    # def processChild(self, childNode, prev, leftmost):
    #     if childNode:
    #         if prev:
    #             prev.next = childNode
    #         else:    
    #             leftmost = childNode
    #         prev = childNode 
    #     return prev, leftmost
    
    # def connect(self, root):
    #     if not root:
    #         return root
    #     leftmost = root
    #     while leftmost:
    #         prev, curr = None, leftmost
    #         leftmost = None
    #         while curr:
    #             prev, leftmost = self.processChild(curr.left, prev, leftmost)
    #             prev, leftmost = self.processChild(curr.right, prev, leftmost)
    #             curr = curr.next
    #     return root 


    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        cur = root
        while cur:
            lc = cur
            while lc:
                if not lc.left and not lc.right:
                    lc = lc.next
                    continue

                next_node = lc.next
                while next_node and not next_node.left and not next_node.right:
                    next_node = next_node.next
                target = next_node and (next_node.left or next_node.right) 
                if lc.left:
                    if lc.right:
                        lc.left.next = lc.right
                        lc.right.next = target
                    else:
                        lc.left.next = target
                else:
                    lc.right.next = target

                lc = lc.next

            this_cur = cur
            cur = None
            while this_cur and not cur:
                cur = this_cur.left or this_cur.right
                this_cur = this_cur.next
                
        return root


        # 不符合空间复杂度要求
        if not root:
            return
        stack = [root]
        while stack:
            new_stack = []
            tar = None
            for i in stack:
                i.next = tar
                tar = i
                if i.right:
                    new_stack.append(i.right)
                if i.left:
                    new_stack.append(i.left)
            stack = new_stack
        return root
        
# @lc code=end

