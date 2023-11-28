/*
 * @lc app=leetcode.cn id=485 lang=golang
 *
 * [485] 最大连续 1 的个数
 *
 * https://leetcode.cn/problems/max-consecutive-ones/description/
 *
 * algorithms
 * Easy (61.09%)
 * Likes:    410
 * Dislikes: 0
 * Total Accepted:    213K
 * Total Submissions: 348.7K
 * Testcase Example:  '[1,1,0,1,1,1]'
 *
 * 给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,1,0,1,1,1]
 * 输出：3
 * 解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
 *
 *
 * 示例 2:
 *
 *
 * 输入：nums = [1,0,1,1,0,1]
 * 输出：2
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 10^5
 * nums[i] 不是 0 就是 1.
 *
 *
 */
package main

// @lc code=start
func findMaxConsecutiveOnes(nums []int) int {
	ans := 0
	cur := 0
	for _, v := range nums {
		if v == 1 {
			cur++
		} else {
			if cur > ans {
				ans = cur
			}
			cur = 0
		}
	}
	if cur > ans {
		ans = cur
	}
	return ans
}

// @lc code=end
