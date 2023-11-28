/*
 * @lc app=leetcode.cn id=572 lang=golang
 *
 * [572] 另一棵树的子树
 *
 * https://leetcode.cn/problems/subtree-of-another-tree/description/
 *
 * algorithms
 * Easy (47.47%)
 * Likes:    974
 * Dislikes: 0
 * Total Accepted:    186.1K
 * Total Submissions: 392.2K
 * Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
 *
 *
 *
 * 给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true
 * ；否则，返回 false 。
 *
 * 二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [3,4,5,1,2], subRoot = [4,1,2]
 * 输出：true
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
 * 输出：false
 *
 *
 *
 *
 * 提示：
 *
 *
 * root 树上的节点数量范围是 [1, 2000]
 * subRoot 树上的节点数量范围是 [1, 1000]
 * -10^4
 * -10^4
 *
 *
 *
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
func isSubtree1(root *TreeNode, subRoot *TreeNode) bool {
	var dfs func(*TreeNode)
	ans := false
	dfs = func(tn *TreeNode) {
		if ans {
			return
		}
		if tn == nil {
			return
		}
		if isSame(tn, subRoot) {
			ans = true
			return
		}
		dfs(tn.Left)
		dfs(tn.Right)
	}
	dfs(root)
	return ans
}

// 迭代
func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
	node := root
	stack := []*TreeNode{}
	for len(stack) > 0 || node != nil {
		for node != nil {
			stack = append(stack, node)
			node = node.Left
		}
		node = stack[len(stack)-1]
		if isSame(node, subRoot) {
			return true
		}
		stack = stack[0 : len(stack)-1]
		node = node.Right
	}
	return false
}

func isSame(n1, n2 *TreeNode) bool {
	if n1 == nil && n2 == nil {
		return true
	}
	if n1 == nil || n2 == nil {
		return false
	}
	if n1.Val != n2.Val {
		return false
	}
	return isSame(n1.Left, n2.Left) && isSame(n1.Right, n2.Right)
}

// @lc code=end
