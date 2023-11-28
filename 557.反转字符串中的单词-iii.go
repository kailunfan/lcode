/*
 * @lc app=leetcode.cn id=557 lang=golang
 *
 * [557] 反转字符串中的单词 III
 *
 * https://leetcode.cn/problems/reverse-words-in-a-string-iii/description/
 *
 * algorithms
 * Easy (73.71%)
 * Likes:    566
 * Dislikes: 0
 * Total Accepted:    313.6K
 * Total Submissions: 425.5K
 * Testcase Example:  `"Let's take LeetCode contest"`
 *
 * 给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "Let's take LeetCode contest"
 * 输出："s'teL ekat edoCteeL tsetnoc"
 *
 *
 * 示例 2:
 *
 *
 * 输入： s = "God Ding"
 * 输出："doG gniD"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 5 * 10^4
 * s 包含可打印的 ASCII 字符。
 * s 不包含任何开头或结尾空格。
 * s 里 至少 有一个词。
 * s 中的所有单词都用一个空格隔开。
 *
 *
 */
package main

// @lc code=start
func reverseWords(s string) string {
	bs := []byte(s)
	start := 0
	for ind, i := range bs {
		if ind == len(s)-1 {
			reverse(bs, start, ind)
		}
		if i == ' ' {
			reverse(bs, start, ind-1)
			start = ind + 1
		}
	}
	return string(bs)
}

// 含头尾
func reverse(bs []byte, start, end int) {
	for start < end {
		bs[start], bs[end] = bs[end], bs[start]
		start++
		end--
	}
}

// @lc code=end
