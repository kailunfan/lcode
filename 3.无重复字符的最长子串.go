/*
 * @lc app=leetcode.cn id=3 lang=golang
 *
 * [3] 无重复字符的最长子串
 */

package main

import "fmt"

// @lc code=start
// 滑动窗口, 双指针
// * 特殊情况特殊处理
// * window重合的情况
// * 减少变量,减少状态
// * 注意window减小的逻辑

func lengthOfLongestSubstring(s string) int {
	// 特殊情况摘除, 简化逻辑
	l := len(s)
	if l <= 1 {
		return l
	}
	ans := 0
	m := map[byte]int{}
	rc := 0
	for i := 0; i < len(s); i++ {
		for rc < len(s) {
			if m[s[rc]] == 1 {
				break
			}
			m[s[rc]] = 1
			rc += 1
		}
		if rc-i > ans {
			ans = rc - i
		}
		delete(m, s[i])
	}
	return ans
}

// @lc code=end

func main() {
	fmt.Println(lengthOfLongestSubstring("abcabcbb"))
	fmt.Println(lengthOfLongestSubstring("mmmm"))
	fmt.Println(lengthOfLongestSubstring("m"))
	fmt.Println(lengthOfLongestSubstring("au"))
}
