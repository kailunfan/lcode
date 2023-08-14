/*
 * @lc app=leetcode.cn id=78 lang=golang
 *
 * [78] 子集
 *
 * https://leetcode.cn/problems/subsets/description/
 *
 * algorithms
 * Medium (81.11%)
 * Likes:    2090
 * Dislikes: 0
 * Total Accepted:    648K
 * Total Submissions: 798.8K
 * Testcase Example:  '[1,2,3]'
 *
 * 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
 *
 * 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,3]
 * 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [0]
 * 输出：[[],[0]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * -10
 * nums 中的所有元素 互不相同
 *
 *
 */
package main

// @lc code=start
func subsets(nums []int) [][]int {
	ans := [][]int{}
	var backTrack func(int, []int)
	backTrack = func(ind int, val []int) {
		ans = append(ans, val)
		for i := ind; i < len(nums); i++ {
			backTrack(i+1, append([]int{nums[i]},val...))
		}
	}
	backTrack(0, []int{})
	return ans
}

func subsets1(nums []int) [][]int {
	ans := [][]int{[]int{}}
	for _, i := range nums {
		for _, a := range ans[:] {
			ans = append(ans, append(append([]int{}, a...), i))
		}
	}
	return ans
}

// @lc code=end
