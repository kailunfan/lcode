/*
 * @lc app=leetcode.cn id=101 lang=golang
 *
 * [101] 对称二叉树
 *
 * https://leetcode.cn/problems/symmetric-tree/description/
 *
 * algorithms
 * Easy (58.54%)
 * Likes:    2247
 * Dislikes: 0
 * Total Accepted:    753.1K
 * Total Submissions: 1.3M
 * Testcase Example:  '[1,2,2,3,4,4,3]'
 *
 * 给你一个二叉树的根节点 root ， 检查它是否轴对称。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [1,2,2,3,4,4,3]
 * 输出：true
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = [1,2,2,null,3,null,3]
 * 输出：false
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中节点数目在范围 [1, 1000] 内
 * -100 <= Node.val <= 100
 *
 *
 *
 *
 * 进阶：你可以运用递归和迭代两种方法解决这个问题吗？
 *
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
package main
// iteration
func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}
	q := []*TreeNode{}
	q = append(q, root)
	q = append(q, root)
	for len(q)>0 {
		n1, n2 := q[0], q[1]
		q = q[2:]
		if n1 == nil && n2 == nil {
			continue
		}
		if n1 == nil || n2 == nil {
			return false
		}
		if n1.Val != n2.Val {
			return false
		}
		q = append(q, n1.Left)
		q = append(q, n2.Right)
		q = append(q, n1.Right)
		q = append(q, n2.Left)
	}
	return true
}

// recursion
func isSymmetric1(root *TreeNode) bool {
	if root == nil {
		return true
	}
	return check(root.Left, root.Right)
}

func check(p, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	}
	if p == nil || q == nil {
		return false
	}
	if p.Val != q.Val {
		return false
	}
	return check(p.Left, q.Right) && check(p.Right, q.Left)
}

// @lc code=end

