/*
 * @lc app=leetcode.cn id=504 lang=golang
 *
 * [504] 七进制数
 *
 * https://leetcode.cn/problems/base-7/description/
 *
 * algorithms
 * Easy (51.76%)
 * Likes:    210
 * Dislikes: 0
 * Total Accepted:    89.5K
 * Total Submissions: 173K
 * Testcase Example:  '100'
 *
 * 给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: num = 100
 * 输出: "202"
 *
 *
 * 示例 2:
 *
 *
 * 输入: num = -7
 * 输出: "-10"
 *
 *
 *
 *
 * 提示：
 *
 *
 * -10^7 <= num <= 10^7
 *
 *
 */
package main

// @lc code=start
func convertToBase7(num int) string {
	if num == 0 {
		return "0"
	}
	neg := num < 0
	if neg {
		num = -num
	}
	s := []byte{}
	for num > 0 {
		s = append(s, '0'+byte(num%7))
		num = num / 7
	}
	for i, j := 0, len(s)-1; i < j; {
		s[i], s[j] = s[j], s[i]
		i++
		j--
	}
	ans := string(s)
	if neg {
		ans = "-" + ans
	}
	return ans
}

// @lc code=end
