/*
 * @lc app=leetcode.cn id=783 lang=golang
 *
 * [783] 二叉搜索树节点最小距离
 *
 * https://leetcode.cn/problems/minimum-distance-between-bst-nodes/description/
 *
 * algorithms
 * Easy (60.15%)
 * Likes:    275
 * Dislikes: 0
 * Total Accepted:    88.7K
 * Total Submissions: 147.5K
 * Testcase Example:  '[4,2,6,1,3]'
 *
 * 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
 *
 * 差值是一个正数，其数值等于两值之差的绝对值。
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [4,2,6,1,3]
 * 输出：1
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = [1,0,48,null,null,12,49]
 * 输出：1
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中节点的数目范围是 [2, 100]
 * 0 <= Node.val <= 10^5
 *
 *
 *
 *
 * 注意：本题与
 * 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
 * 相同
 *
 *
 *
 */
package main

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func minDiffInBST(root *TreeNode) int {
	prevVal := math.MaxInt32
	diff := math.MaxInt32
	cur := root
	stack := []*TreeNode{}
	for cur != nil || len(stack) > 0 {
		for cur != nil {
			stack = append(stack, cur)
			cur = cur.Left
		}
		cur = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		thisDiff := diffInt(prevVal, cur.Val)
		if thisDiff < diff {
			diff = thisDiff
		}
		prevVal = cur.Val
		cur = cur.Right
	}
	return diff
}

func diffInt(a, b int) int {
	if a-b > 0 {
		return a - b
	}
	return b - a
}

// @lc code=end
