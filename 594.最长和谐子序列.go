/*
 * @lc app=leetcode.cn id=594 lang=golang
 *
 * [594] 最长和谐子序列
 *
 * https://leetcode.cn/problems/longest-harmonious-subsequence/description/
 *
 * algorithms
 * Easy (56.21%)
 * Likes:    391
 * Dislikes: 0
 * Total Accepted:    86.5K
 * Total Submissions: 153.9K
 * Testcase Example:  '[1,3,2,2,5,2,3,7]'
 *
 * 和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。
 *
 * 现在，给你一个整数数组 nums ，请你在所有可能的子序列中找到最长的和谐子序列的长度。
 *
 * 数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,3,2,2,5,2,3,7]
 * 输出：5
 * 解释：最长的和谐子序列是 [3,2,2,2,3]
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1,2,3,4]
 * 输出：2
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [1,1,1,1]
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * -10^9
 *
 *
 */
package main

// @lc code=start
func findLHS(nums []int) int {
	m := map[int]int{}
	for _, i := range nums {
		m[i]++
	}
	ans := 0
	for num, c := range m {
		if c1 := m[num+1]; c1 > 0 && c+c1 > ans {
			ans = c + c1
		}
	}
	return ans

}

// @lc code=end
