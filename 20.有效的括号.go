/*
 * @lc app=leetcode.cn id=20 lang=golang
 *
 * [20] 有效的括号
 *
 * https://leetcode.cn/problems/valid-parentheses/description/
 *
 * algorithms
 * Easy (44.05%)
 * Likes:    4032
 * Dislikes: 0
 * Total Accepted:    1.5M
 * Total Submissions: 3.5M
 * Testcase Example:  '"()"'
 *
 * 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
 *
 * 有效字符串需满足：
 *
 *
 * 左括号必须用相同类型的右括号闭合。
 * 左括号必须以正确的顺序闭合。
 * 每个右括号都有一个对应的相同类型的左括号。
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "()"
 * 输出：true
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "()[]{}"
 * 输出：true
 *
 *
 * 示例 3：
 *
 *
 * 输入：s = "(]"
 * 输出：false
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 10^4
 * s 仅由括号 '()[]{}' 组成
 *
 *
 */
package main

// @lc code=start
func isValid(s string) bool {
	l := len(s)
	if l%2 != 0 {
		return false
	}
	m := map[rune]rune{
		'(': ')',
		'[': ']',
		'{': '}',
	}
	stack := []rune{}
	for _, i := range s {
		if len(stack) == 0 {
			stack = append(stack, i)
			continue
		}
		
		last := stack[len(stack)-1]
		if m[last] == i {
			stack = stack[:len(stack)-1]
		} else {
			stack = append(stack, i)
		}
	}
	if len(stack) == 0 {
		return true
	}
	return false
}

// @lc code=end
