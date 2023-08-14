/*
 * @lc app=leetcode.cn id=77 lang=golang
 *
 * [77] 组合
 *
 * https://leetcode.cn/problems/combinations/description/
 *
 * algorithms
 * Medium (77.11%)
 * Likes:    1429
 * Dislikes: 0
 * Total Accepted:    559.9K
 * Total Submissions: 726.3K
 * Testcase Example:  '4\n2'
 *
 * 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
 *
 * 你可以按 任何顺序 返回答案。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 4, k = 2
 * 输出：
 * [
 * ⁠ [2,4],
 * ⁠ [3,4],
 * ⁠ [2,3],
 * ⁠ [1,2],
 * ⁠ [1,3],
 * ⁠ [1,4],
 * ]
 *
 * 示例 2：
 *
 *
 * 输入：n = 1, k = 1
 * 输出：[[1]]
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * 1
 *
 *
 */
package main

// @lc code=start
func combine(n int, k int) [][]int {
	ans := [][]int{[]int{}}
	for i := 1; i < n+1; i++ {
		for _, a := range ans[:] {
			if len(a) < k {
				ans = append(ans, append(append([]int{}, a...), i))
			}
		}
	}
	res := [][]int{}
	for _, i := range ans {
		if len(i) == k {
			res = append(res, i)
		}
	}

	return res
}

func combine1(n int, k int) [][]int {
	ans := [][]int{}
	var backTrack func(ind int, tmp []int)
	backTrack = func(ind int, tmp []int) {
		if len(tmp) == k {
			ans = append(ans, append([]int{}, tmp...))
		}
		for i := ind + 1; i <= n; i++ {
			// backTrack(i, append(append([]int{}, tmp...), i))
			backTrack(i, append([]int{i}, tmp...))
		}
	}
	backTrack(0, []int{})
	return ans
}

// @lc code=end
