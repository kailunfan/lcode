/*
 * @lc app=leetcode.cn id=228 lang=golang
 *
 * [228] 汇总区间
 *
 * https://leetcode.cn/problems/summary-ranges/description/
 *
 * algorithms
 * Easy (54.48%)
 * Likes:    276
 * Dislikes: 0
 * Total Accepted:    100.3K
 * Total Submissions: 184.5K
 * Testcase Example:  '[0,1,2,4,5,7]'
 *
 * 给定一个  无重复元素 的 有序 整数数组 nums 。
 *
 * 返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于
 * nums 的数字 x 。
 *
 * 列表中的每个区间范围 [a,b] 应该按如下格式输出：
 *
 *
 * "a->b" ，如果 a != b
 * "a" ，如果 a == b
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [0,1,2,4,5,7]
 * 输出：["0->2","4->5","7"]
 * 解释：区间范围是：
 * [0,2] --> "0->2"
 * [4,5] --> "4->5"
 * [7,7] --> "7"
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [0,2,3,4,6,8,9]
 * 输出：["0","2->4","6","8->9"]
 * 解释：区间范围是：
 * [0,0] --> "0"
 * [2,4] --> "2->4"
 * [6,6] --> "6"
 * [8,9] --> "8->9"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= nums.length <= 20
 * -2^31 <= nums[i] <= 2^31 - 1
 * nums 中的所有值都 互不相同
 * nums 按升序排列
 *
 *
 */
package main

import "fmt"

/*
考察点:
1. 开始位置:因为长度为1也是结果的一部分, 所以要从0位置就开始;
2. 结束位置;
3. 输出结果条件;
*/

// @lc code=start
func summaryRanges(nums []int) []string {
	if len(nums) == 0 {
		return []string{}
	}
	ans := []string{}
	start := 0
	for i := 0; i < len(nums); i++ {
		/**
		when to add ans?
		- 到终点
		- 不连续
		*/
		// if i == len(nums)-1 {
		// 	if i == start {
		// 		ans = append(ans, fmt.Sprintf("%d", nums[start]))
		// 	} else {
		// 		ans = append(ans, fmt.Sprintf("%d->%d", nums[start], nums[i]))
		// 	}
		// 	break
		// }

		// if nums[i+1]-nums[i] > 1 {
		// 	if i == start {
		// 		ans = append(ans, fmt.Sprintf("%d", nums[start]))
		// 	} else {
		// 		ans = append(ans, fmt.Sprintf("%d->%d", nums[start], nums[i]))
		// 	}
		// 	start = i + 1
		// }
		// 以上条件可进行合并
		if i == len(nums)-1 || nums[i+1]-nums[i] > 1 {
			if i == start {
				ans = append(ans, fmt.Sprintf("%d", nums[start]))
			} else {
				ans = append(ans, fmt.Sprintf("%d->%d", nums[start], nums[i]))
			}
			start = i + 1
		}
	}
	return ans
}

// @lc code=end
