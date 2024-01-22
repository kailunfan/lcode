/*
 * @lc app=leetcode.cn id=696 lang=golang
 *
 * [696] 计数二进制子串
 *
 * https://leetcode.cn/problems/count-binary-substrings/description/
 *
 * algorithms
 * Easy (63.63%)
 * Likes:    540
 * Dislikes: 0
 * Total Accepted:    74K
 * Total Submissions: 116.4K
 * Testcase Example:  '"00110011"'
 *
 * 给定一个字符串 s，统计并返回具有相同数量 0 和 1 的非空（连续）子字符串的数量，并且这些子字符串中的所有 0 和所有 1 都是成组连续的。
 *
 * 重复出现（不同位置）的子串也要统计它们出现的次数。
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "00110011"
 * 输出：6
 * 解释：6 个子串满足具有相同数量的连续 1 和 0 ："0011"、"01"、"1100"、"10"、"0011" 和 "01" 。
 * 注意，一些重复出现的子串（不同位置）要统计它们出现的次数。
 * 另外，"00110011" 不是有效的子串，因为所有的 0（还有 1 ）没有组合在一起。
 *
 * 示例 2：
 *
 *
 * 输入：s = "10101"
 * 输出：4
 * 解释：有 4 个子串："10"、"01"、"10"、"01" ，具有相同数量的连续 1 和 0 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 10^5
 * s[i] 为 '0' 或 '1'
 *
 *
 */
package main

// @lc code=start
func countBinarySubstrings(s string) int {
	g := []int{}
	v, count := s[0], 1
	for i := 1; i < len(s); i++ {
		if s[i] == v {
			count++
		} else {
			g = append(g, count)
			count = 1
			v = s[i]
		}
	}
	g = append(g, count)
	ans := 0
	for i := 0; i < len(g)-1; i++ {
		ans += min(g[i], g[i+1])
	}
	return ans
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

// @lc code=end
