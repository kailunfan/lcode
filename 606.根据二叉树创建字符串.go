/*
 * @lc app=leetcode.cn id=606 lang=golang
 *
 * [606] 根据二叉树创建字符串
 *
 * https://leetcode.cn/problems/construct-string-from-binary-tree/description/
 *
 * algorithms
 * Easy (62.06%)
 * Likes:    387
 * Dislikes: 0
 * Total Accepted:    76.3K
 * Total Submissions: 123.1K
 * Testcase Example:  '[1,2,3,4]'
 *
 * 给你二叉树的根节点 root ，请你采用前序遍历的方式，将二叉树转化为一个由括号和整数组成的字符串，返回构造出的字符串。
 *
 * 空节点使用一对空括号对 "()" 表示，转化后需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [1,2,3,4]
 * 输出："1(2(4))(3)"
 * 解释：初步转化后得到 "1(2(4)())(3()())" ，但省略所有不必要的空括号对后，字符串应该是"1(2(4))(3)" 。
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = [1,2,3,null,4]
 * 输出："1(2()(4))(3)"
 * 解释：和第一个示例类似，但是无法省略第一个空括号对，否则会破坏输入与输出一一映射的关系。
 *
 *
 *
 * 提示：
 *
 *
 * 树中节点的数目范围是 [1, 10^4]
 * -1000 <= Node.val <= 1000
 *
 *
 *
 *
 */
package main

import "strings"
import "strconv"

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
func tree2str(root *TreeNode) string {
	// ans := []string{}
	ans := strings.Builder{}
	var dfs func(node *TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			return
		}
		ans.WriteString(strconv.Itoa(node.Val))
		// 如何组织条件语句?
		// 1. 按条件组织行为
		// 2. 按行为组织条件
		if node.Left != nil || node.Right != nil {
			ans.WriteString("(")
			dfs(node.Left)
			ans.WriteString(")")
		}
		if node.Right != nil {
			ans.WriteString("(")
			dfs(node.Right)
			ans.WriteString(")")
		}
	}
	dfs(root)
	return ans.String()
}

// @lc code=end
