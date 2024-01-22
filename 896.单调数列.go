/*
 * @lc app=leetcode.cn id=896 lang=golang
 *
 * [896] 单调数列
 *
 * https://leetcode.cn/problems/monotonic-array/description/
 *
 * algorithms
 * Easy (56.89%)
 * Likes:    204
 * Dislikes: 0
 * Total Accepted:    91.9K
 * Total Submissions: 161.7K
 * Testcase Example:  '[1,2,2,3]'
 *
 * 如果数组是单调递增或单调递减的，那么它是 单调 的。
 *
 * 如果对于所有 i <= j，nums[i] <= nums[j]，那么数组 nums 是单调递增的。 如果对于所有 i <= j，nums[i]> =
 * nums[j]，那么数组 nums 是单调递减的。
 *
 * 当给定的数组 nums 是单调数组时返回 true，否则返回 false。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,2,3]
 * 输出：true
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [6,5,4,4]
 * 输出：true
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [1,3,2]
 * 输出：false
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 10^5
 * -10^5 <= nums[i] <= 10^5
 *
 *
 */
package main

// @lc code=start
func isMonotonic(nums []int) bool {
	orderFlag := 0
	l := len(nums)
	for i := 0; i <= l-2; i++ {
		if nums[i] < nums[i+1] {
			if orderFlag == 2 {
				return false
			}
			orderFlag = 1
		} else if nums[i] > nums[i+1] {
			if orderFlag == 1 {
				return false
			}
			orderFlag = 2
		}
	}
	return true
}

// @lc code=end
