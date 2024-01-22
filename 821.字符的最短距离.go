/*
 * @lc app=leetcode.cn id=821 lang=golang
 *
 * [821] 字符的最短距离
 *
 * https://leetcode.cn/problems/shortest-distance-to-a-character/description/
 *
 * algorithms
 * Easy (72.78%)
 * Likes:    352
 * Dislikes: 0
 * Total Accepted:    77.3K
 * Total Submissions: 106.2K
 * Testcase Example:  '"loveleetcode"\n"e"'
 *
 * 给你一个字符串 s 和一个字符 c ，且 c 是 s 中出现过的字符。
 *
 * 返回一个整数数组 answer ，其中 answer.length == s.length 且 answer[i] 是 s 中从下标 i 到离它 最近
 * 的字符 c 的 距离 。
 *
 * 两个下标 i 和 j 之间的 距离 为 abs(i - j) ，其中 abs 是绝对值函数。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "loveleetcode", c = "e"
 * 输出：[3,2,1,0,1,0,0,1,2,2,1,0]
 * 解释：字符 'e' 出现在下标 3、5、6 和 11 处（下标从 0 开始计数）。
 * 距下标 0 最近的 'e' 出现在下标 3 ，所以距离为 abs(0 - 3) = 3 。
 * 距下标 1 最近的 'e' 出现在下标 3 ，所以距离为 abs(1 - 3) = 2 。
 * 对于下标 4 ，出现在下标 3 和下标 5 处的 'e' 都离它最近，但距离是一样的 abs(4 - 3) == abs(4 - 5) = 1 。
 * 距下标 8 最近的 'e' 出现在下标 6 ，所以距离为 abs(8 - 6) = 2 。
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "aaab", c = "b"
 * 输出：[3,2,1,0]
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 10^4
 * s[i] 和 c 均为小写英文字母
 * 题目数据保证 c 在 s 中至少出现一次
 *
 *
 */
package main

// @lc code=start
func shortestToChar(s string, c byte) []int {
	targetIndex := []int{}
	target := rune(c)
	for i, v := range s {
		if v == target {
			targetIndex = append(targetIndex, i)
		}
	}
	ans := []int{}
	for i := 0; i < len(s); i++ {
		for j := 0; i < len(targetIndex); j++ {
			if j == 0 {
				if i <= targetIndex[j] {
					ans = append(ans, targetIndex[j]-i)
				}
				continue
			}
			if j == len(targetIndex)-1 {
				if i > targetIndex[j] {
					ans = append(ans, i-targetIndex[j])
				}
				continue
			}
			if i > targetIndex[j] && i <= targetIndex[j+1] {
				ans = append(ans, min(targetIndex[j+1]-i, i-targetIndex[j]))
			}
		}
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
