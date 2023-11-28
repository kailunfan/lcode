/*
 * @lc app=leetcode.cn id=530 lang=golang
 *
 * [530] 二叉搜索树的最小绝对差
 *
 * https://leetcode.cn/problems/minimum-absolute-difference-in-bst/description/
 *
 * algorithms
 * Easy (63.36%)
 * Likes:    508
 * Dislikes: 0
 * Total Accepted:    199.6K
 * Total Submissions: 315.4K
 * Testcase Example:  '[4,2,6,1,3]'
 *
 * 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
 *
 * 差值是一个正数，其数值等于两值之差的绝对值。
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
 * 树中节点的数目范围是 [2, 10^4]
 * 0 <= Node.val <= 10^5
 *
 *
 *
 *
 * 注意：本题与 783
 * https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同
 *
 */
package main

import "math"

// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func diffInt(a, b int) int {
	if a-b > 0 {
		return a - b
	}
	return b - a
}

func getMinimumDifference(root *TreeNode) int {
	stack := []*TreeNode{}
	cur := root
	prevVal := math.MaxInt32
	diff := math.MaxInt32
	ans := []*TreeNode{}
	for len(stack) > 0 || cur != nil {
		for cur != nil {
			stack = append(stack, cur)
			cur = cur.Left
		}
		cur = stack[len(stack)-1]
		stack = stack[0 : len(stack)-1]
		thisDiff := diffInt(prevVal, cur.Val)
		if thisDiff < diff {
			diff = thisDiff
		}
		prevVal = cur.Val
		ans = append(ans, cur)
		cur = cur.Right
	}
	return diff
}

// @lc code=end
