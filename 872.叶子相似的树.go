/*
* @lc app=leetcode.cn id=872 lang=golang
*
* [872] 叶子相似的树
*
* https://leetcode.cn/problems/leaf-similar-trees/description/
*
  - algorithms
  - Easy (65.12%)
  - Likes:    227
  - Dislikes: 0
  - Total Accepted:    83.9K
  - Total Submissions: 128.8K
  - Testcase Example:  '[3,5,1,6,2,9,8,null,null,7,4]\n' +
    '[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'

*
* 请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
*
*
*
* 举个例子，如上图所示，给定一棵叶值序列为 (6, 7, 4, 9, 8) 的树。
*
* 如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
*
* 如果给定的两个根结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。
*
*
*
* 示例 1：
*
*
*
*
* 输入：root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 =
* [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
* 输出：true
*
*
* 示例 2：
*
*
*
*
* 输入：root1 = [1,2,3], root2 = [1,3,2]
* 输出：false
*
*
*
*
* 提示：
*
*
* 给定的两棵树结点数在 [1, 200] 范围内
* 给定的两棵树上的值在 [0, 200] 范围内
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
func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	var s func(node *TreeNode) []int
	s = func(node *TreeNode) []int {
		if node == nil {
			return []int{}
		}
		if node.Left == nil && node.Right == nil {
			return []int{node.Val}
		}
		return append(s(node.Left), s(node.Right)...)
	}
	v1 := s(root1)
	v2 := s(root2)
	if len(v1) != len(v2) {
		return false
	}
	for i := range v1 {
		if v1[i] != v2[i] {
			return false
		}
	}
	return true
}

// @lc code=end
