/*
 * @lc app=leetcode.cn id=693 lang=golang
 *
 * [693] 交替位二进制数
 *
 * https://leetcode.cn/problems/binary-number-with-alternating-bits/description/
 *
 * algorithms
 * Easy (65.15%)
 * Likes:    234
 * Dislikes: 0
 * Total Accepted:    80.6K
 * Total Submissions: 123.7K
 * Testcase Example:  '5'
 *
 * 给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 5
 * 输出：true
 * 解释：5 的二进制表示是：101
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 7
 * 输出：false
 * 解释：7 的二进制表示是：111.
 *
 * 示例 3：
 *
 *
 * 输入：n = 11
 * 输出：false
 * 解释：11 的二进制表示是：1011.
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
func hasAlternatingBits(n int) bool {
	prev := -1
	v := 0
	for n > 0 {
		v = n % 2
		if prev != -1 && v == prev {
			return false
		}
		prev = v
		n = n / 2
	}
	return true
}

// @lc code=end
