/*
 * @lc app=leetcode.cn id=409 lang=golang
 *
 * [409] 最长回文串
 *
 * https://leetcode.cn/problems/longest-palindrome/description/
 *
 * algorithms
 * Easy (55.76%)
 * Likes:    550
 * Dislikes: 0
 * Total Accepted:    180.5K
 * Total Submissions: 323.8K
 * Testcase Example:  '"abccccdd"'
 *
 * 给定一个包含大写字母和小写字母的字符串 s ，返回 通过这些字母构造成的 最长的回文串 。
 *
 * 在构造过程中，请注意 区分大小写 。比如 "Aa" 不能当做一个回文字符串。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入:s = "abccccdd"
 * 输出:7
 * 解释:
 * 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
 *
 *
 * 示例 2:
 *
 *
 * 输入:s = "a"
 * 输出:1
 *
 *
 * 示例 3：
 *
 *
 * 输入:s = "aaaaaccc"
 * 输出:7
 *
 *
 *
 * 提示:
 *
 *
 * 1 <= s.length <= 2000
 * s 只由小写 和/或 大写英文字母组成
 *
 *
 */
package main

// @lc code=start
func longestPalindrome(s string) int {
	counter := map[rune]int{}
	for _, i := range s {
		counter[i] += 1
	}
	ans := 0
	for _, v := range counter {
		ans += v / 2 * 2
	}
	if ans < len(s) {
		ans += 1
	}
	return ans
}

// @lc code=end
