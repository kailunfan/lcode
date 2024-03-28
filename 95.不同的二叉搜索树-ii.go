/*
 * @lc app=leetcode.cn id=95 lang=golang
 *
 * [95] 不同的二叉搜索树 II
 *
 * https://leetcode.cn/problems/unique-binary-search-trees-ii/description/
 *
 * algorithms
 * Medium (73.09%)
 * Likes:    1371
 * Dislikes: 0
 * Total Accepted:    157.1K
 * Total Submissions: 215K
 * Testcase Example:  '3'
 *
 * 给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 3
 * 输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 1
 * 输出：[[1]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 *
 *
 *
 *
 */
package main

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
func generateTrees(n int) []*TreeNode {
	var dfs func(start, end int) []*TreeNode
	dfs = func(start, end int) []*TreeNode {
		if start > end {
			return []*TreeNode{nil}
		}
		if start == end {
			return []*TreeNode{&TreeNode{Val: start}}
		}
		ans := []*TreeNode{}
		for i := start; i <= end; i++ {
			for _, j := range dfs(start, i-1) {
				for _, k := range dfs(i+1, end) {
					ans = append(ans, &TreeNode{Val: i, Left: j, Right: k})
				}
			}
		}
		return ans
	}
	return dfs(1, n)
}

// @lc code=end
