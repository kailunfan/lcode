/*
 * @lc app=leetcode.cn id=111 lang=golang
 *
 * [111] 二叉树的最小深度
 *
 * https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
 *
 * algorithms
 * Easy (42.07%)
 * Likes:    257
 * Dislikes: 0
 * Total Accepted:    75.9K
 * Total Submissions: 178.9K
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * 给定一个二叉树，找出其最小深度。
 * 
 * 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
 * 
 * 说明: 叶子节点是指没有子节点的节点。
 * 
 * 示例:
 * 
 * 给定二叉树 [3,9,20,null,null,15,7],
 * 
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 * 
 * 返回它的最小深度  2.
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
func minDepth(root *TreeNode) int {
	if root == nil{
		return 0
	}
	q := []*TreeNode{}
	q = append(q,root)
	ans := 1

	for(q != nil){
		tmp:=[]*TreeNode{}
		for i:=0;i<len(q);i++{
			node := q[i]
			if node.Left == nil && node.Right == nil{
				return ans 
			}
			if node.Left != nil{
				tmp = append(tmp,node.Left)
			}
			if node.Right!=nil{
				tmp = append(tmp,node.Right)
			}
		}
		ans++
		q = tmp
	}
	return ans
}
// @lc code=end

