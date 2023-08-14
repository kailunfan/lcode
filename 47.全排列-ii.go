/*
 * @lc app=leetcode.cn id=47 lang=golang
 *
 * [47] 全排列 II
 *
 * https://leetcode.cn/problems/permutations-ii/description/
 *
 * algorithms
 * Medium (65.52%)
 * Likes:    1383
 * Dislikes: 0
 * Total Accepted:    461.7K
 * Total Submissions: 704.6K
 * Testcase Example:  '[1,1,2]'
 *
 * 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,1,2]
 * 输出：
 * [[1,1,2],
 * ⁠[1,2,1],
 * ⁠[2,1,1]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1,2,3]
 * 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 8
 * -10 <= nums[i] <= 10
 *
 *
 */
package main

// @lc code=start
func permuteUnique(nums []int) [][]int {
	ans := [][]int{}
	var backTrack func(int)
	backTrack = func(ind int) {
		if ind == len(nums)-1 {
			ans = append(ans, append([]int{}, nums...))
		}
		for i := ind; i < len(nums); i++ {
			nums[i], nums[ind] = nums[ind], nums[i]
			backTrack(ind + 1)
			nums[i], nums[ind] = nums[ind], nums[i]
		}
	}
	backTrack(0)
	return ans
}

// @lc code=end
