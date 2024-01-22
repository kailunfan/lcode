/*
 * @lc app=leetcode.cn id=917 lang=golang
 *
 * [917] 仅仅反转字母
 *
 * https://leetcode.cn/problems/reverse-only-letters/description/
 *
 * algorithms
 * Easy (59.31%)
 * Likes:    209
 * Dislikes: 0
 * Total Accepted:    81.4K
 * Total Submissions: 137.2K
 * Testcase Example:  '"ab-cd"'
 *
 * 给你一个字符串 s ，根据下述规则反转字符串：
 *
 *
 * 所有非英文字母保留在原有位置。
 * 所有英文字母（小写或大写）位置反转。
 *
 *
 * 返回反转后的 s 。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "ab-cd"
 * 输出："dc-ba"
 *
 *
 *
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "a-bC-dEf-ghIj"
 * 输出："j-Ih-gfE-dCba"
 *
 *
 *
 *
 *
 * 示例 3：
 *
 *
 * 输入：s = "Test1ng-Leet=code-Q!"
 * 输出："Qedo1ct-eeLg=ntse-T!"
 *
 *
 *
 *
 * 提示
 *
 *
 * 1 <= s.length <= 100
 * s 仅由 ASCII 值在范围 [33, 122] 的字符组成
 * s 不含 '\"' 或 '\\'
 *
 *
 */
package main

import "unicode"

// @lc code=start
func reverseOnlyLetters(s string) string {
	l, r := 0, len(s)-1
	ans := []byte(s)
	for l < r {
		for l < r && !unicode.IsLetter(rune(s[l])) {
			l++
		}
		for l < r && !unicode.IsLetter(rune(s[r])) {
			r--
		}
		ans[l], ans[r] = ans[r], ans[l]
		l++
		r--
	}
	return string(ans)
}


// @lc code=end
