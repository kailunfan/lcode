/*
 * @lc app=leetcode.cn id=92 lang=golang
 *
 * [92] 反转链表 II
 *
 * https://leetcode.cn/problems/reverse-linked-list-ii/description/
 *
 * algorithms
 * Medium (55.64%)
 * Likes:    1552
 * Dislikes: 0
 * Total Accepted:    394.1K
 * Total Submissions: 708.3K
 * Testcase Example:  '[1,2,3,4,5]\n2\n4'
 *
 * 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left  。请你反转从位置 left 到位置 right 的链表节点，返回
 * 反转后的链表 。
 *
 *
 * 示例 1：
 *
 *
 * 输入：head = [1,2,3,4,5], left = 2, right = 4
 * 输出：[1,4,3,2,5]
 *
 *
 * 示例 2：
 *
 *
 * 输入：head = [5], left = 1, right = 1
 * 输出：[5]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 链表中节点数目为 n
 * 1
 * -500
 * 1
 *
 *
 *
 *
 * 进阶： 你可以使用一趟扫描完成反转吗？
 *
 */

/**
 * Definition for singly-linked list.
 * type ListNode struct {
	 *     Val int
	 *     Next *ListNode
	 * }
*/
package main

type ListNode struct {
	Val  int
	Next *ListNode
}

// @lc code=start

func reverseBetween(head *ListNode, left int, right int) *ListNode {
	sentry := &ListNode{Next: head}
	lc := sentry
	for i := 0; i < left-1; i++ {
		lc = lc.Next
	}
	cur := lc.Next
	var pre *ListNode
	tmp := cur
	for i := 0; i < right-left+1; i++ {
		cur.Next, cur, pre = pre, cur.Next, cur
	}
	lc.Next = pre
	tmp.Next = cur
	
	return sentry.Next
}

// @lc code=end
