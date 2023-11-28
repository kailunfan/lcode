/*
 * @lc app=leetcode.cn id=70 lang=golang
 *
 * [70] 爬楼梯
 *
 * https://leetcode-cn.com/problems/climbing-stairs/description/
 *
 * algorithms
 * Easy (53.60%)
 * Likes:    2453
 * Dislikes: 0
 * Total Accepted:    847.6K
 * Total Submissions: 1.6M
 * Testcase Example:  '2'
 *
 * 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
 *
 * 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 2
 * 输出：2
 * 解释：有两种方法可以爬到楼顶。
 * 1. 1 阶 + 1 阶
 * 2. 2 阶
 *
 * 示例 2：
 *
 *
 * 输入：n = 3
 * 输出：3
 * 解释：有三种方法可以爬到楼顶。
 * 1. 1 阶 + 1 阶 + 1 阶
 * 2. 1 阶 + 2 阶
 * 3. 2 阶 + 1 阶
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 45
 *
 *
 */
package main

// @lc code=start
func climbStairs(n int) int {
	if n <= 2 {
		return n
	}
	s1, s2 := 1, 2
	for i := 3; i <= n; i++ {
		s1, s2 = s2, s1+s2
	}
	return s2
}

// recrusive, may be timeout
func climbStairs1(n int) int {
	if n <= 2 {
		return n
	}
	return climbStairs(n-1) + climbStairs(n-2)
}

// @lc code=end
