/*
 * @lc app=leetcode.cn id=144 lang=golang
 *
 * [144] 二叉树的前序遍历
 *
 * https://leetcode.cn/problems/binary-tree-preorder-traversal/description/
 *
 * algorithms
 * Easy (71.29%)
 * Likes:    979
 * Dislikes: 0
 * Total Accepted:    776.4K
 * Total Submissions: 1.1M
 * Testcase Example:  '[1,null,2,3]'
 *
 * 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [1,null,2,3]
 * 输出：[1,2,3]
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = []
 * 输出：[]
 *
 *
 * 示例 3：
 *
 *
 * 输入：root = [1]
 * 输出：[1]
 *
 *
 * 示例 4：
 *
 *
 * 输入：root = [1,2]
 * 输出：[1,2]
 *
 *
 * 示例 5：
 *
 *
 * 输入：root = [1,null,2]
 * 输出：[1,2]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中节点数目在范围 [0, 100] 内
 * -100
 *
 *
 *
 *
 * 进阶：递归算法很简单，你可以通过迭代算法完成吗？
 *
 */
package main
// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func preorderTraversal1(root *TreeNode) (ans []int) {
	var fc func(node *TreeNode)
	fc = func(node *TreeNode) {
		if node == nil {
			return
		}
		ans = append(ans, node.Val)
		fc(node.Left)
		fc(node.Right)
	}
	fc(root)
	return
}

func preorderTraversal(root *TreeNode) (ans []int) {
	stack := []*TreeNode{}
	for root != nil || len(stack)>0 {
		for root != nil{
			stack = append(stack, root)
			ans = append(ans, root.Val)
			root = root.Left
		}
		root = stack[len(stack)-1]
		stack = stack[0:len(stack)-1]
		root = root.Right
	}
	return
}

// @lc code=end

