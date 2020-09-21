#
# @lc app=leetcode.cn id=863 lang=python3
#
# [863] 二叉树中所有距离为 K 的结点
#
# https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/description/
#
# algorithms
# Medium (48.27%)
# Likes:    98
# Dislikes: 0
# Total Accepted:    5K
# Total Submissions: 10.2K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n2'
#
# 给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。
#
# 返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。
#
#
#
#
#
#
# 示例 1：
#
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
#
# 输出：[7,4,1]
#
# 解释：
# 所求结点为与目标结点（值为 5）距离为 2 的结点，
# 值分别为 7，4，以及 1
#
#
#
# 注意，输入的 "root" 和 "target" 实际上是树上的结点。
# 上面的输入仅仅是对这些对象进行了序列化描述。
#
#
#
#
# 提示：
#
#
# 给定的树是非空的，且最多有 K 个结点。
# 树上的每个结点都具有唯一的值 0 <= node.val <= 500 。
# 目标结点 target 是树上的结点。
# 0 <= K <= 1000.
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
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if not root:
            return []
        # 遍历添加父指针
        root.par = None
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                node.left.par = node
            if node.right:
                stack.append(node.right)
                node.right.par = node

        # 广度遍历
        ans = [target]
        visited = set()
        for i in range(K):
            tmp = []
            for node in ans:
                visited.add(node)
                for attr in ['left', 'right', 'par']:
                    n = getattr(node,attr)
                    if not n or n in visited:
                        continue
                    tmp.append(n)
            ans = tmp
        return [x.val for x in ans]


# @lc code=end
