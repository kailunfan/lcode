/*
 * @lc app=leetcode.cn id=34 lang=golang
 *
 * [34] 在排序数组中查找元素的第一个和最后一个位置
 *
 * https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/
 *
 * algorithms
 * Medium (42.35%)
 * Likes:    2309
 * Dislikes: 0
 * Total Accepted:    791.8K
 * Total Submissions: 1.9M
 * Testcase Example:  '[5,7,7,8,8,10]\n8'
 *
 * 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
 *
 * 如果数组中不存在目标值 target，返回 [-1, -1]。
 *
 * 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [5,7,7,8,8,10], target = 8
 * 输出：[3,4]
 *
 * 示例 2：
 *
 *
 * 输入：nums = [5,7,7,8,8,10], target = 6
 * 输出：[-1,-1]
 *
 * 示例 3：
 *
 *
 * 输入：nums = [], target = 0
 * 输出：[-1,-1]
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= nums.length <= 10^5
 * -10^9 <= nums[i] <= 10^9
 * nums 是一个非递减数组
 * -10^9 <= target <= 10^9
 *
 *
 */
package main

// @lc code=start
/*
1. 二分寻找第一个[0,l-1]
2. 二分寻找最后一个[m,l-1]
**/
func searchRange(nums []int, target int) []int {
	if len(nums) == 0 {
		return []int{-1, -1}
	}

	// search min
	lc, rc := 0, len(nums)-1
	for lc < rc {
		m := (lc + rc) / 2
		v := nums[m]
		if v < target {
			lc = m + 1
		} else {
			rc = m
		}
	}
	if nums[lc] != target {
		return []int{-1, -1}
	}

	mn := lc

	// search max
	lc, rc = mn, len(nums)-1
	for lc < rc {
		// lc=m时 m 需+1, 防止死循环, eg: 0+1//2 = 0
		m := (lc + rc + 1) / 2
		if nums[m] > target {
			rc = m - 1
		} else {
			lc = m
		}
	}
	mx := lc
	return []int{mn, mx}
}

// @lc code=end
