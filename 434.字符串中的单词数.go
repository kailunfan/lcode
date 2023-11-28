/*
 * @lc app=leetcode.cn id=434 lang=golang
 *
 * [434] 字符串中的单词数
 *
 * https://leetcode.cn/problems/number-of-segments-in-a-string/description/
 *
 * algorithms
 * Easy (38.54%)
 * Likes:    216
 * Dislikes: 0
 * Total Accepted:    94.1K
 * Total Submissions: 244.3K
 * Testcase Example:  '"Hello, my name is John"'
 *
 * 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
 *
 * 请注意，你可以假定字符串里不包括任何不可打印的字符。
 *
 * 示例:
 *
 * 输入: "Hello, my name is John"
 * 输出: 5
 * 解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。
 *
 *
 */
package main

// @lc code=start
func countSegments(s string) int {
	state := true
	ans := 0
	for _, i := range s {
		if i != ' ' {
			if state {
				ans += 1
			}
			state = false
		} else {
			state = true
		}
	}
	return ans
}

// @lc code=end
