/*
 * @lc app=leetcode.cn id=22 lang=golang
 *
 * [22] 括号生成
 *
 * https://leetcode.cn/problems/generate-parentheses/description/
 *
 * algorithms
 * Medium (77.45%)
 * Likes:    3295
 * Dislikes: 0
 * Total Accepted:    716.4K
 * Total Submissions: 925K
 * Testcase Example:  '3'
 *
 * 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 3
 * 输出：["((()))","(()())","(())()","()(())","()()()"]
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 1
 * 输出：["()"]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 8
 *
 *
 */
package main

// @lc code=start
func generateParenthesis(n int) []string {
	ans := make([]string, 0)
	var backTrack func(int, int, string)
	backTrack = func(lc, rc int, tmp string) {
		if lc == n && rc == n {
			ans = append(ans, tmp)
			return
		}
		if lc < n {
			backTrack(lc+1, rc, tmp+"(")
		}
		if lc > rc {
			backTrack(lc, rc+1, tmp+")")
		}
	}

	backTrack(0, 0, "")
	return ans
}

// @lc code=end

func generateParenthesis_wrong(n int) []string {
	ans_set := make(map[string]struct{})
	var backTrack func(int, string)
	backTrack = func(ind int, tmp string) {
		if ind == n {
			ans_set[tmp] = struct{}{}
			return
		}
		// 这种思路是错误的,反例  (())(())
		backTrack(ind+1, "("+tmp+")")
		backTrack(ind+1, "()"+tmp)
		backTrack(ind+1, tmp+"()")
	}
	backTrack(0, "")
	ans := []string{}
	for k := range ans_set {
		ans = append(ans, k)
	}
	return ans
}
