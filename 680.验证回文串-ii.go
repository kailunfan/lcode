/*
 * @lc app=leetcode.cn id=680 lang=golang
 *
 * [680] 验证回文串 II
 *
 * https://leetcode.cn/problems/valid-palindrome-ii/description/
 *
 * algorithms
 * Easy (40.09%)
 * Likes:    620
 * Dislikes: 0
 * Total Accepted:    142.4K
 * Total Submissions: 355.2K
 * Testcase Example:  '"aba"'
 *
 * 给你一个字符串 s，最多 可以从中删除一个字符。
 *
 * 请你判断 s 是否能成为回文字符串：如果能，返回 true ；否则，返回 false 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "aba"
 * 输出：true
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "abca"
 * 输出：true
 * 解释：你可以删除字符 'c' 。
 *
 *
 * 示例 3：
 *
 *
 * 输入：s = "abc"
 * 输出：false
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 10^5
 * s 由小写英文字母组成
 *
 *
 */
package main

// @lc code=start
func validPalindrome1(s string) bool {
	use := false
	var search func(int, int) bool
	search = func(lc, rc int) bool {
		if lc >= rc {
			return true
		}
		if s[lc] == s[rc] {
			return search(lc+1, rc-1)
		}
		if use {
			return false
		}
		use = true
		return search(lc+1, rc) || search(lc, rc-1)
	}
	return search(0, len(s)-1)
}

func validPalindrome(s string) bool {
	lc, rc := 0, len(s)-1
	for lc < rc {
		if s[lc] == s[rc] {
			lc++
			rc--
		} else {
			return isPalindrome(s[lc+1:rc+1]) || isPalindrome(s[lc:rc])
		}
	}
	return true
}

func isPalindrome(s string) bool {
	lc, rc := 0, len(s)-1
	for lc < rc {
		if s[lc] != s[rc] {
			return false
		}
		lc++
		rc--
	}
	return true
}

// @lc code=end
