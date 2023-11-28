/*
 * @lc app=leetcode.cn id=441 lang=golang
 *
 * [441] 排列硬币
 *
 * https://leetcode.cn/problems/arranging-coins/description/
 *
 * algorithms
 * Easy (45.19%)
 * Likes:    282
 * Dislikes: 0
 * Total Accepted:    123.9K
 * Total Submissions: 274.2K
 * Testcase Example:  '5'
 *
 * 你总共有 n 枚硬币，并计划将它们按阶梯状排列。对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的。
 *
 * 给你一个数字 n ，计算并返回可形成 完整阶梯行 的总行数。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 5
 * 输出：2
 * 解释：因为第三行不完整，所以返回 2 。
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 8
 * 输出：3
 * 解释：因为第四行不完整，所以返回 3 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 2^31 - 1
 *
 *
 */
package main

// @lc code=start
/*
1. 为什么 l=mid 而不是 l = mid+1, 因为mid可能就是结果, +1会造成错过结果;
2. 为什么 mid := (l + r + 1) / 2 而不是 (l + r) / 2, 考虑到1的前提和 (0,1)的情况,不+1会造成死循环.
*/
func arrangeCoins(n int) int {
	l, r := 1, n
	for l < r {
		mid := (l + r + 1) / 2
		need := mid * (mid + 1)
		if need <= n*2 {
			l = mid
		} else {
			r = mid - 1
		}
	}
	return l
}

// @lc code=end
