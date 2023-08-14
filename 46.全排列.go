/*
 * @lc app=leetcode.cn id=46 lang=golang
 *
 * [46] 全排列
 *
 * https://leetcode.cn/problems/permutations/description/
 *
 * algorithms
 * Medium (78.88%)
 * Likes:    2578
 * Dislikes: 0
 * Total Accepted:    875.5K
 * Total Submissions: 1.1M
 * Testcase Example:  '[1,2,3]'
 *
 * 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,3]
 * 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [0,1]
 * 输出：[[0,1],[1,0]]
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [1]
 * 输出：[[1]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 6
 * -10 <= nums[i] <= 10
 * nums 中的所有整数 互不相同
 *
 *
 */
package main

// @lc code=start

func permute1(nums []int) [][]int {
	ans := [][]int{}
	var backTrack func(int)
	backTrack = func(ind int) {
		if ind == len(nums)-1 {
			// 要复制一份出来
			ans = append(ans, append([]int{}, nums...))
		}
		for i := ind; i < len(nums); i++ {
			// 排列逻辑
			nums[ind], nums[i] = nums[i], nums[ind]
			backTrack(ind + 1)
			// 恢复
			nums[ind], nums[i] = nums[i], nums[ind]
		}
	}
	backTrack(0)
	return ans
}

func permute(nums []int) [][]int {
	ans := [][]int{[]int{}}
	for _, i := range nums {
		thisAns := [][]int{}
		for _, j := range ans {
			for k := 0; k <= len(j); k++ {
				newItem := []int{}
				newItem = append(newItem, j[:k]...)
				newItem = append(newItem, i)
				newItem = append(newItem, j[k:]...)
				thisAns = append(thisAns, newItem)
			}
		}
		ans = thisAns
	}
	return ans
}

// @lc code=end
