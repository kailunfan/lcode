/*
 * @lc app=leetcode.cn id=628 lang=golang
 *
 * [628] 三个数的最大乘积
 *
 * https://leetcode.cn/problems/maximum-product-of-three-numbers/description/
 *
 * algorithms
 * Easy (51.95%)
 * Likes:    467
 * Dislikes: 0
 * Total Accepted:    124.3K
 * Total Submissions: 239.4K
 * Testcase Example:  '[1,2,3]'
 *
 * 给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,3]
 * 输出：6
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1,2,3,4]
 * 输出：24
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [-1,-2,-3]
 * 输出：-6
 *
 *
 *
 *
 * 提示：
 *
 *
 * 3
 * -1000
 *
 *
 */
package main

import "math"

// 数学, heap
// @lc code=start
func maximumProduct(nums []int) int {
	max1, max2, max3 := math.MinInt, math.MinInt, math.MinInt
	min1, min2 := math.MaxInt, math.MaxInt
	for _, x := range nums {
		if x > max1 {
			max1, max2, max3 = x, max1, max2
		} else if x > max2 {
			max2, max3 = x, max2
		} else if x > max3 {
			max3 = x
		}
		if x < min1 {
			min1, min2 = x, min1
		} else if x < min2 {
			min2 = x
		}
	}
	return max(max1*max2*max3, min1*min2*max1)
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

// @lc code=end
