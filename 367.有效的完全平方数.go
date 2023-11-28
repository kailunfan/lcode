/*
 * @lc app=leetcode.cn id=367 lang=golang
 *
 * [367] 有效的完全平方数
 *
 * https://leetcode.cn/problems/valid-perfect-square/description/
 *
 * algorithms
 * Easy (44.82%)
 * Likes:    525
 * Dislikes: 0
 * Total Accepted:    234.6K
 * Total Submissions: 523.5K
 * Testcase Example:  '16'
 *
 * 给你一个正整数 num 。如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
 *
 * 完全平方数 是一个可以写成某个整数的平方的整数。换句话说，它可以写成某个整数和自身的乘积。
 *
 * 不能使用任何内置的库函数，如  sqrt 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：num = 16
 * 输出：true
 * 解释：返回 true ，因为 4 * 4 = 16 且 4 是一个整数。
 *
 *
 * 示例 2：
 *
 *
 * 输入：num = 14
 * 输出：false
 * 解释：返回 false ，因为 3.742 * 3.742 = 14 但 3.742 不是一个整数。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= num <= 2^31 - 1
 *
 *
 */
package main

import "math"

// 二分查找
// @lc code=start
func isPerfectSquare(num int) bool {
	x := int(math.Sqrt(float64(num)))
	return x*x == num

	// lc, rc := 0, num

	// for lc < rc {
	// 	mid := (rc + rc) / 2
	// 	square := mid * mid
	// 	if square < num {
	// 		lc = mid + 1
	// 	} else if square > num {
	// 		rc = mid - 2
	// 	} else {
	// 		return true
	// 	}
	// }
	// return false
}

// @lc code=end
