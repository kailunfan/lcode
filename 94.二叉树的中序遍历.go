/*
 * @lc app=leetcode.cn id=94 lang=golang
 *
 * [94] 二叉树的中序遍历
 *
 * https://leetcode.cn/problems/binary-tree-inorder-traversal/description/
 *
 * algorithms
 * Easy (75.90%)
 * Likes:    1668
 * Dislikes: 0
 * Total Accepted:    1M
 * Total Submissions: 1.4M
 * Testcase Example:  '[1,null,2,3]'
 *
 * 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [1,null,2,3]
 * 输出：[1,3,2]
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
 *
 *
 * 提示：
 *
 *
 * 树中节点数目在范围 [0, 100] 内
 * -100 <= Node.val <= 100
 *
 *
 *
 *
 * 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
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
func inorderTraversal1(root *TreeNode) []int {
	var ans []int
	if root == nil {
		return ans
	}
	ans = append(ans, inorderTraversal(root.Left)...)
	ans = append(ans, root.Val)
	ans = append(ans, inorderTraversal(root.Right)...)
	return ans
}

func inorderTraversal2(root *TreeNode) (ans []int) {
	var fc func(node *TreeNode)
	fc = func(node *TreeNode){
		if node == nil {
			return
		}
		fc(node.Left)
		ans = append(ans, node.Val)
		fc(node.Right)
	}
	fc(root)
	return
}

// iteration
func inorderTraversal(root *TreeNode) (ans []int) {
	stack := []*TreeNode{}
	for root != nil || len(stack) > 0 {
		for root != nil{
			stack = append(stack, root)
			root = root.Left
		}
		root = stack[len(stack)-1]
		stack = stack[0:len(stack)-1]
		ans = append(ans, root.Val)
		root = root.Right
	}
	return
}

// @lc code=end

