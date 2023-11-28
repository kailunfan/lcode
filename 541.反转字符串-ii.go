/*
 * @lc app=leetcode.cn id=541 lang=golang
 *
 * [541] 反转字符串 II
 *
 * https://leetcode.cn/problems/reverse-string-ii/description/
 *
 * algorithms
 * Easy (57.74%)
 * Likes:    536
 * Dislikes: 0
 * Total Accepted:    229.9K
 * Total Submissions: 398.3K
 * Testcase Example:  '"abcdefg"\n2'
 *
 * 给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。
 *
 *
 * 如果剩余字符少于 k 个，则将剩余字符全部反转。
 * 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "abcdefg", k = 2
 * 输出："bacdfeg"
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "abcd", k = 2
 * 输出："bacd"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 10^4
 * s 仅由小写英文组成
 * 1 <= k <= 10^4
 *
 *
 */
package main

// @lc code=start
func reverseStr(s string, k int) string {
	t := []byte(s)
	for i := 0; i < len(s); i += 2 * k {
		reverse(t, i, i+k)
	}
	return string(t)
}

func reverse(t []byte, start, end int) {
	if end > len(t) {
		end = len(t)
	}
	// ! ** 注意边界, 含头不含尾. 与切片操作保持一致
	end--
	for start < end {
		t[start], t[end] = t[end], t[start]
		start++
		end--
	}
}

// @lc code=end
