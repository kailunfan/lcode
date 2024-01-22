/*
* @lc app=leetcode.cn id=703 lang=golang
*
* [703] 数据流中的第 K 大元素
*
* https://leetcode.cn/problems/kth-largest-element-in-a-stream/description/
*
  - algorithms
  - Easy (52.49%)
  - Likes:    454
  - Dislikes: 0
  - Total Accepted:    94.8K
  - Total Submissions: 180.5K
  - Testcase Example:  '["KthLargest","add","add","add","add","add"]\n' +
    '[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]'

*
* 设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。
*
* 请实现 KthLargest 类：
*
*
* KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
* int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。
*
*
*
*
* 示例：
*
*
* 输入：
* ["KthLargest", "add", "add", "add", "add", "add"]
* [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
* 输出：
* [null, 4, 5, 5, 8, 8]
*
* 解释：
* KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
* kthLargest.add(3);   // return 4
* kthLargest.add(5);   // return 5
* kthLargest.add(10);  // return 5
* kthLargest.add(9);   // return 8
* kthLargest.add(4);   // return 8
*
*
*
* 提示：
*
*
* 1
* 0
* -10^4
* -10^4
* 最多调用 add 方法 10^4 次
* 题目数据保证，在查找第 k 大元素时，数组中至少有 k 个元素
*
*
*/
package main

import "fmt"

// @lc code=start
type KthLargest struct {
	k      int
	k_list []int
}

func Constructor(k int, nums []int) KthLargest {
	kList := []int{}
	for _, v := range nums {
		kList = insert(kList, v, k)
	}
	fmt.Println(kList)
	return KthLargest{k, kList}
}

func (this *KthLargest) Add(val int) int {
	this.k_list = insert(this.k_list, val, this.k)
	return this.k_list[this.k-1]
}

func insert(nums []int, v int, max int) []int {
	if len(nums) == 0 {
		return []int{v}
	}

	if v >= nums[0] {
		nums = append([]int{v}, nums...)
		if len(nums) > max {
			nums = nums[0 : len(nums)-1]
		}
		return nums
	}
    
	if v <= nums[len(nums)-1] {
		if len(nums) >= max {
			return nums
		}
		return append(nums, v)
	}

	for i := 1; i < len(nums); i++ {
		if v <= nums[i-1] && v >= nums[i] {
			nums = append(nums[0:i], append([]int{v}, nums[i:]...)...)
			if len(nums) > max {
				nums = nums[0 : len(nums)-1]
			}
			break
		}
	}
	return nums
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * obj := Constructor(k, nums);
 * param_1 := obj.Add(val);
 */
// @lc code=end
