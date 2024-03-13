/*
 * @lc app=leetcode.cn id=2 lang=golang
 *
 * [2] 两数相加
 */

package main

type ListNode struct {
	Val  int
	Next *ListNode
}

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
	cur := sentry
	carry := 0
	for l1 != nil || l2 != nil || carry != 0 {
		s := carry
		if l1 != nil {
			s += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			s += l2.Val
			l2 = l2.Next
		}
		carry = s / 10
		cur.Next = &ListNode{Val: s % 10}
		cur = cur.Next
	}
	return sentry.Next
}

// @lc code=end
