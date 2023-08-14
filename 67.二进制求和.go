/*
 * @lc app=leetcode.cn id=67 lang=golang
 *
 * [67] 二进制求和
 *
 * https://leetcode.cn/problems/add-binary/description/
 *
 * algorithms
 * Easy (52.94%)
 * Likes:    1062
 * Dislikes: 0
 * Total Accepted:    334.1K
 * Total Submissions: 631.1K
 * Testcase Example:  '"11"\n"1"'
 *
 * 给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入:a = "11", b = "1"
 * 输出："100"
 *
 * 示例 2：
 *
 *
 * 输入：a = "1010", b = "1011"
 * 输出："10101"
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= a.length, b.length <= 10^4
 * a 和 b 仅由字符 '0' 或 '1' 组成
 * 字符串如果不是 "0" ，就不含前导零
 *
 *
 */
package main

import "strconv"

// @lc code=start
func addBinary(a string, b string) string {
	ans := ""
	carry := 0
	la, lb := len(a), len(b)

	for i := 1; ; i++ {
		aind := la - i
		bind := lb - i
		if aind < 0 && bind < 0 && carry == 0 {
			break
		}
		add := carry
		if aind >= 0 {
			add += int(a[aind] - '0')
		}
		if bind >= 0 {
			add += int(b[bind] - '0')
		}
		carry = add / 2
		ans = strconv.Itoa(add%2) + ans
	}
	return ans
}

// @lc code=end
