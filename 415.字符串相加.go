/*
 * @lc app=leetcode.cn id=415 lang=golang
 *
 * [415] 字符串相加
 *
 * https://leetcode.cn/problems/add-strings/description/
 *
 * algorithms
 * Easy (54.75%)
 * Likes:    788
 * Dislikes: 0
 * Total Accepted:    298.9K
 * Total Submissions: 546K
 * Testcase Example:  '"11"\n"123"'
 *
 * 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。
 *
 * 你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：num1 = "11", num2 = "123"
 * 输出："134"
 *
 *
 * 示例 2：
 *
 *
 * 输入：num1 = "456", num2 = "77"
 * 输出："533"
 *
 *
 * 示例 3：
 *
 *
 * 输入：num1 = "0", num2 = "0"
 * 输出："0"
 *
 *
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= num1.length, num2.length <= 10^4
 * num1 和num2 都只包含数字 0-9
 * num1 和num2 都不包含任何前导零
 *
 *
 */
package main

import "strconv"


// @lc code=start
func addStrings1(num1 string, num2 string) string {
	c1, c2 := len(num1)-1, len(num2)-1
	carry := 0
	ans := ""
	for carry > 0 || c1 >= 0 || c2 >= 0 {
		sum := carry
		if c1 >= 0 {
			sum += int(num1[c1] - '0')
		}
		if c2 >= 0 {
			sum += int(num2[c2] - '0')
		}
		ans = strconv.Itoa(sum%10) + ans
		carry = sum / 10
		c1--
		c2--
	}
	return ans
}

// @lc code=end
