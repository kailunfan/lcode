/*
 * @lc app=leetcode.cn id=905 lang=golang
 *
 * [905] 按奇偶排序数组
 *
 * https://leetcode.cn/problems/sort-array-by-parity/description/
 *
 * algorithms
 * Easy (70.99%)
 * Likes:    379
 * Dislikes: 0
 * Total Accepted:    128.4K
 * Total Submissions: 180.9K
 * Testcase Example:  '[3,1,2,4]'
 *
 * 给你一个整数数组 nums，将 nums 中的的所有偶数元素移动到数组的前面，后跟所有奇数元素。
 *
 * 返回满足此条件的 任一数组 作为答案。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [3,1,2,4]
 * 输出：[2,4,3,1]
 * 解释：[4,2,3,1]、[2,4,1,3] 和 [4,2,1,3] 也会被视作正确答案。
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [0]
 * 输出：[0]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 5000
 * 0 <= nums[i] <= 5000
 *
 *
 */
package main

// @lc code=start
func sortArrayByParity(nums []int) []int {
	if len(nums) == 0 {
		return nums
	}
	lc, rc := 0, len(nums)-1
	for lc < rc {
		for nums[lc]%2 == 0 && lc < rc {
			lc++
		}
		for nums[rc]%2 == 1 && lc < rc {
			rc--
		}
		nums[lc], nums[rc] = nums[rc], nums[lc]
	}
	return nums
}

// @lc code=end
