/*
 * @lc app=leetcode.cn id=66 lang=golang
 *
 * [66] 加一
 *
 * https://leetcode.cn/problems/plus-one/description/
 *
 * algorithms
 * Easy (45.11%)
 * Likes:    1258
 * Dislikes: 0
 * Total Accepted:    648.1K
 * Total Submissions: 1.4M
 * Testcase Example:  '[1,2,3]'
 *
 * 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
 *
 * 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
 *
 * 你可以假设除了整数 0 之外，这个整数不会以零开头。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：digits = [1,2,3]
 * 输出：[1,2,4]
 * 解释：输入数组表示数字 123。
 *
 *
 * 示例 2：
 *
 *
 * 输入：digits = [4,3,2,1]
 * 输出：[4,3,2,2]
 * 解释：输入数组表示数字 4321。
 *
 *
 * 示例 3：
 *
 *
 * 输入：digits = [0]
 * 输出：[1]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * 0
 *
 *
 */
package main

// @lc code=start
func plusOne(digits []int) []int {
	jump := 1
	for i := len(digits) - 1; i >= 0; i-- {
		add := digits[i] + jump
		digits[i] = add % 10
		jump = add / 10
	}
	if jump == 1 {
		digits = append([]int{1}, digits...)
	}
	return digits
}

// @lc code=end
