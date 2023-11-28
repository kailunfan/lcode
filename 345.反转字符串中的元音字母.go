/*
 * @lc app=leetcode.cn id=345 lang=golang
 *
 * [345] 反转字符串中的元音字母
 *
 * https://leetcode.cn/problems/reverse-vowels-of-a-string/description/
 *
 * algorithms
 * Easy (54.53%)
 * Likes:    319
 * Dislikes: 0
 * Total Accepted:    174.3K
 * Total Submissions: 319.7K
 * Testcase Example:  '"hello"'
 *
 * 给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。
 *
 * 元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现不止一次。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "hello"
 * 输出："holle"
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "leetcode"
 * 输出："leotcede"
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 3 * 10^5
 * s 由 可打印的 ASCII 字符组成
 *
 *
 */
package main

// @lc code=start
func reverseVowels(s string) string {
	if len(s) == 0 {
		return s
	}
	s1 := []byte(s)
	vowelSet := map[byte]struct{}{'a': struct{}{}, 'e': struct{}{}, 'i': struct{}{}, 'o': struct{}{}, 'u': struct{}{}, 'A': struct{}{}, 'E': struct{}{}, 'I': struct{}{}, 'O': struct{}{}, 'U': struct{}{}}
	lc, rc := 0, len(s1)-1
	for lc < rc {
		swap := true
		if _, ok := vowelSet[s1[lc]]; !ok {
			swap = false
			lc++
		}
		if _, ok := vowelSet[s1[rc]]; !ok {
			swap = false
			rc--
		}
		if swap {
			s1[lc], s1[rc] = s1[rc], s1[lc]
			lc++
			rc--
		}
	}
	return string(s1)
}

// @lc code=end
