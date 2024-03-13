/*
 * @lc app=leetcode.cn id=1072 lang=golang
 *
 * [1072] 按列翻转得到最大值等行数
 *
 * https://leetcode.cn/problems/flip-columns-for-maximum-number-of-equal-rows/description/
 *
 * algorithms
 * Medium (71.43%)
 * Likes:    148
 * Dislikes: 0
 * Total Accepted:    21.9K
 * Total Submissions: 30.7K
 * Testcase Example:  '[[0,1],[1,1]]'
 *
 * 给定 m x n 矩阵 matrix 。
 *
 * 你可以从中选出任意数量的列并翻转其上的 每个 单元格。（即翻转后，单元格的值从 0 变成 1，或者从 1 变为 0 。）
 *
 * 返回 经过一些翻转后，行内所有值都相等的最大行数 。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：matrix = [[0,1],[1,1]]
 * 输出：1
 * 解释：不进行翻转，有 1 行所有值都相等。
 *
 *
 * 示例 2：
 *
 *
 * 输入：matrix = [[0,1],[1,0]]
 * 输出：2
 * 解释：翻转第一列的值之后，这两行都由相等的值组成。
 *
 *
 * 示例 3：
 *
 *
 * 输入：matrix = [[0,0,0],[0,0,1],[1,1,0]]
 * 输出：2
 * 解释：翻转前两列的值之后，后两行由相等的值组成。
 *
 *
 *
 * 提示：
 *
 *
 * m == matrix.length
 * n == matrix[i].length
 * 1 <= m, n <= 300
 * matrix[i][j] == 0 或 1
 *
 *
 */
package main

import "strings"

// @lc code=start
func maxEqualRowsAfterFlips(matrix [][]int) int {
	m := map[string]int{}
	for _, row := range matrix {
		if row[0] == 1 {
			for j := range row {
				row[j] ^= 1
			}
		}
		m[hash(row)]++
	}

	max := 0
	for _, v := range m {
		if v > max {
			max = v
		}
	}
	return max
}

func hash(row []int) string {
	var s strings.Builder
	for _, v := range row {
		s.WriteString(string(v))
	}
	return s.String()
}

// @lc code=end
