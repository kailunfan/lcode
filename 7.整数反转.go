/*
 * @lc app=leetcode.cn id=7 lang=golang
 *
 * [7] 整数反转
 *
 * https://leetcode.cn/problems/reverse-integer/description/
 *
 * algorithms
 * Medium (35.30%)
 * Likes:    3532
 * Dislikes: 0
 * Total Accepted:    1M
 * Total Submissions: 2.9M
 * Testcase Example:  '-123'
 *
 * 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
 *
 * 如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
 * 假设环境不允许存储 64 位整数（有符号或无符号）。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：x = 123
 * 输出：321
 *
 *
 * 示例 2：
 *
 *
 * 输入：x = -123
 * 输出：-321
 *
 *
 * 示例 3：
 *
 *
 * 输入：x = 120
 * 输出：21
 *
 *
 * 示例 4：
 *
 *
 * 输入：x = 0
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * -2^31
 *
 *
 */
package main

import "math"

// @lc code=start
func reverse(x int) int {
	ans := 0
	for x != 0 {
		// ! 边界条件要怎么处理?
		// 判断某数乘以 10 是否会溢出，那么就把该数和 INT_MAX 除以 10 进行比较。
		if ans < math.MinInt32/10 || ans > math.MaxInt32/10 {
			return 0
		}
		remain := x % 10
		ans = ans*10 + remain
		x /= 10
	}
	return ans
}

// @lc code=end
