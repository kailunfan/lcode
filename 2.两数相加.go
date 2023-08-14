/*
 * @lc app=leetcode.cn id=2 lang=golang
 *
 * [2] 两数相加
 */

package main
 

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	sentry := new(ListNode)
	lr := sentry
	carry := 0
	for {
		// 优化
		if l1 == nil && carry == 0 {
			lr.Next = l2
			break
		}
		if l2 == nil && carry == 0 {
			lr.Next = l1
			break
		}

		v1, v2 := 0, 0
		if l1 != nil {
			v1 = l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			v2 = l2.Val
			l2 = l2.Next
		}
		sum := v1 + v2 + carry
		carry = sum / 10
		val := sum % 10
		lr.Next = &ListNode{Val: val}
		lr = lr.Next
	}
	return sentry.Next
}

// @lc code=end
