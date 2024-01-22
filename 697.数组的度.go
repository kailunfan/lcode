/*
 * @lc app=leetcode.cn id=697 lang=golang
 *
 * [697] 数组的度
 *
 * https://leetcode.cn/problems/degree-of-an-array/description/
 *
 * algorithms
 * Easy (59.17%)
 * Likes:    489
 * Dislikes: 0
 * Total Accepted:    96.4K
 * Total Submissions: 162.9K
 * Testcase Example:  '[1,2,2,3,1]'
 *
 * 给定一个非空且只包含非负数的整数数组 nums，数组的 度 的定义是指数组里任一元素出现频数的最大值。
 *
 * 你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,2,3,1]
 * 输出：2
 * 解释：
 * 输入数组的度是 2 ，因为元素 1 和 2 的出现频数最大，均为 2 。
 * 连续子数组里面拥有相同度的有如下所示：
 * [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
 * 最短连续子数组 [2, 2] 的长度为 2 ，所以返回 2 。
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1,2,2,3,1,4,2]
 * 输出：6
 * 解释：
 * 数组的度是 3 ，因为元素 2 重复出现 3 次。
 * 所以 [2,2,3,1,4,2] 是最短子数组，因此返回 6 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * nums.length 在 1 到 50,000 范围内。
 * nums[i] 是一个在 0 到 49,999 范围内的整数。
 *
 *
 */
package main

// @lc code=start
type entry struct {
	count, lp, rp int
}

func findShortestSubArray(nums []int) int {
	m := map[int]entry{}
	for i, v := range nums {
		if item, ok := m[v]; ok {
			item.rp = i
			item.count++
			// go 太反直觉了, 可怕, 这行必不可少.
			m[v] = item
		} else {
			m[v] = entry{1, i, i}
		}
	}
	maxCount := 0
	ans := 0
	for _, v := range m {
		if v.count > maxCount {
			maxCount = v.count
			ans = v.rp - v.lp + 1
		} else if v.count == maxCount {
			ans = min(v.rp - v.lp + 1, ans)
		}
	}

	return ans
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

// @lc code=end
