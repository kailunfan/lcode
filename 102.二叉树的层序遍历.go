/*
 * @lc app=leetcode.cn id=102 lang=golang
 *
 * [102] 二叉树的层序遍历
 *
 * https://leetcode.cn/problems/binary-tree-level-order-traversal/description/
 *
 * algorithms
 * Medium (65.36%)
 * Likes:    1556
 * Dislikes: 0
 * Total Accepted:    735.7K
 * Total Submissions: 1.1M
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [3,9,20,null,null,15,7]
 * 输出：[[3],[9,20],[15,7]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = [1]
 * 输出：[[1]]
 *
 *
 * 示例 3：
 *
 *
 * 输入：root = []
 * 输出：[]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中节点数目在范围 [0, 2000] 内
 * -1000 <= Node.val <= 1000
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
// package main

// type TreeNode struct {
//     Val int
//     Left *TreeNode
//     Right *TreeNode

// }

func levelOrder(root *TreeNode) [][]int {
	ans := [][]int{}
	if root == nil {
		return ans
	}
	layer := []*TreeNode{root}
	for len(layer) > 0 {
		thisLayer := []*TreeNode{}
		thisAns := []int{}
		for _, x := range layer {
			thisAns = append(thisAns, x.Val)
			if x.Left != nil {
				thisLayer = append(thisLayer, x.Left)
			}
			if x.Right != nil {
				thisLayer = append(thisLayer, x.Right)
			}
		}
		ans = append(ans, thisAns)
		layer = thisLayer
	}
	return ans
}

// @lc code=end

