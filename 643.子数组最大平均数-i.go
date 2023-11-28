/*
 * @lc app=leetcode.cn id=643 lang=golang
 *
 * [643] 子数组最大平均数 I
 *
 * https://leetcode.cn/problems/maximum-average-subarray-i/description/
 *
 * algorithms
 * Easy (43.15%)
 * Likes:    326
 * Dislikes: 0
 * Total Accepted:    121.8K
 * Total Submissions: 282.6K
 * Testcase Example:  '[1,12,-5,-6,50,3]\n4'
 *
 * 给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。
 *
 * 请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。
 *
 * 任何误差小于 10^-5 的答案都将被视为正确答案。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,12,-5,-6,50,3], k = 4
 * 输出：12.75
 * 解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [5], k = 1
 * 输出：5.00000
 *
 *
 *
 *
 * 提示：
 *
 *
 * n == nums.length
 * 1 <= k <= n <= 10^5
 * -10^4 <= nums[i] <= 10^4
 *
 *
 */
package main

/*
滑动窗口:
1. 构造窗口. 注意末尾指针位置: 超出了窗口
2. 滑动窗口. 结束条件;

条件最好放在for中, 避免可能出现的数组越界.
*/


// @lc code=start
func findMaxAverage(nums []int, k int) float64 {
	sum := 0
	lc, rc := 0, 0
	for rc < k {
		sum += nums[rc]
		rc++
	}

	maxSum := sum
	for rc < len(nums) {
		sum = sum + nums[rc] - nums[lc]
		maxSum = max(maxSum, sum)
		lc++
		rc++
	}
	return float64(maxSum) / float64(k)
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

// @lc code=end
