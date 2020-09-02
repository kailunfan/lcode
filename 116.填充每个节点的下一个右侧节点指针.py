#
# @lc app=leetcode.cn id=116 lang=python
#
# [116] 填充每个节点的下一个右侧节点指针
#
# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/description/
#
# algorithms
# Medium (57.69%)
# Likes:    169
# Dislikes: 0
# Total Accepted:    33.7K
# Total Submissions: 56.9K
# Testcase Example:  '[1,2,3,4,5,6,7]'
#
# 给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
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
# 示例：
# 
# 
# 
# 
# 输入：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}
# 
# 
# 输出：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}
# 
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
# 
# 
# 
# 
# 提示：
# 
# 
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
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
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        # 标准解法
        # 下面的方法都不满足事件复杂度要求
        # 该题要借助next指针进行层次搜索

        if not root:
            return

        cur = root
        while cur:
            lc = cur
            while lc:
                if not lc.left:
                    break
                lc.left.next = lc.right
                if lc.next:
                    lc.right.next = lc.next.left
                lc = lc.next
            cur = cur.left
        return root
            
                       


        # 递归
        # def walk(node):
        #     if not node or (not node.left and not node.right):
        #         return
        #     node.left.next = node.right
        #     if node.next:
        #         node.right.next = node.next.left
        #     walk(node.left)
        #     walk(node.right)
        # walk(root)
        # return root

        # 上面递归貌似并没有压结果,应该可以通过简单的方式转化为迭代
        # 深度优先遍历
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if not all([node.left,node.right]):
                continue
            node.left.next = node.right
            # 这是关键点
            if node.next:
                node.right.next = node.next.left
            stack.extend([node.right,node.left])
        return root



        # 广度优先遍历
        if not root:
            return
        q = [root]
        while q:
            node = q.pop(0)
            if not all([node.left,node.right]):
                continue
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left
            q.extend([node.left,node.right])
        return root

        






        # 该解法空间复杂度过高,违反了规则
        if not root:
            return
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root 

        if not root:
            return
        layer = [root]
        while layer:
            tmp = []
            for ind,node in enumerate(layer):
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
                if ind == len(layer) - 1:
                    node.next = None
                else:
                    node.next = layer[ind+1]
            layer = tmp
        
        return root



                
# @lc code=end

