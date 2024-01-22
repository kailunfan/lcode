/*
 * @lc app=leetcode.cn id=867 lang=golang
 *
 * [867] 转置矩阵
 *
 * https://leetcode.cn/problems/transpose-matrix/description/
 *
 * algorithms
 * Easy (66.91%)
 * Likes:    258
 * Dislikes: 0
 * Total Accepted:    105K
 * Total Submissions: 156.8K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * 给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。
 *
 * 矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
 * 输出：[[1,4,7],[2,5,8],[3,6,9]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：matrix = [[1,2,3],[4,5,6]]
 * 输出：[[1,4],[2,5],[3,6]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == matrix.length
 * n == matrix[i].length
 * 1
 * 1
 * -10^9
 *
 *
 */
package main

// @lc code=start
func transpose(matrix [][]int) [][]int {
	n, m := len(matrix), len(matrix[0])
	t := make([][]int, m)
	for i := range t {
		t[i] = make([]int, n)
		for j := range t[i] {
			t[i][j] = 0
		}
	}
	for i := range matrix {
		for j := range matrix[i] {
			t[j][i] = matrix[i][j]
		}
	}
	return t
}

// @lc code=end
