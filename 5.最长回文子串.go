/*
 * @lc app=leetcode.cn id=5 lang=golang
 *
 * [5] 最长回文子串
 *
 * https://leetcode.cn/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (36.74%)
 * Likes:    5301
 * Dislikes: 0
 * Total Accepted:    1.1M
 * Total Submissions: 2.9M
 * Testcase Example:  '"babad"'
 *
 * 给你一个字符串 s，找到 s 中最长的回文子串。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "babad"
 * 输出："bab"
 * 解释："aba" 同样是符合题意的答案。
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "cbbd"
 * 输出："bb"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 1000
 * s 仅由数字和英文字母组成
 *
 *
 */

package main

import "fmt"

// @lc code=start
func longestPalindrome1(s string) string {
	// 动态规划本质上是减少重复计算 --->  方式:规划计算顺序
	l := len(s)
	if l <= 1 {
		return s
	}

	// 初始化
	dp := make([][]bool, len(s))
	for i := 0; i < l; i++ {
		dp[i] = make([]bool, l)
	}

	ans := s[0:1]
	ansLength := 1
	for i := 0; i < l; i++ {
		for j := 0; j < i; j++ {
			if i == j {
				dp[i][j] = true
			}
			if s[i] == s[j] {
				if i-j < 3 {
					dp[i][j] = true
				} else {
					dp[i][j] = dp[i-1][j+1]
				}
			}
			if dp[i][j] && i-j+1 > ansLength {
				ansLength = i - j + 1
				ans = s[j : i+1]
			}
		}
	}
	return ans
}

func longestPalindrome(s string) string {
	// 针对数据结构的特殊解法
	// 对每个字符串进行考察, 以其为中心的回文串长度.
	start, end := 0, 0
	for i := 0; i < len(s); i++ {
		left, right := getPalindrome(s, i, i)
		if right-left > end-start {
			start, end = left, right
		}
		left, right = getPalindrome(s, i, i+1)
		if right-left > end-start {
			start, end = left, right
		}
	}
	return s[start : end+1]
}

// 拆分复杂度
func getPalindrome(s string, left, right int) (int, int) {
	for ; left >= 0 && right < len(s) && s[left] == s[right]; left, right = left-1, right+1 {
	}
	return left + 1, right - 1
}

// @lc code=end
func main() {
	fmt.Println(longestPalindrome("abba"))
}
