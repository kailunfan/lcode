/*
 * @lc app=leetcode.cn id=1 lang=golang
 *
 * [1] 两数之和
 */

package main

// @lc code=start
func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for ind, item := range nums {
		remainder := target - item
		if _, ok := m[remainder]; ok {
			return []int{m[remainder], ind}
		}
		m[item] = ind
	}
	return []int{}
}

// @lc code=end
