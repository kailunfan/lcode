/*
 * @lc app=leetcode.cn id=61 lang=golang
 *
 * [61] 旋转链表
 *
 * https://leetcode.cn/problems/rotate-list/description/
 *
 * algorithms
 * Medium (41.52%)
 * Likes:    913
 * Dislikes: 0
 * Total Accepted:    307.2K
 * Total Submissions: 740K
 * Testcase Example:  '[1,2,3,4,5]\n2'
 *
 * 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：head = [1,2,3,4,5], k = 2
 * 输出：[4,5,1,2,3]
 *
 *
 * 示例 2：
 *
 *
 * 输入：head = [0,1,2], k = 4
 * 输出：[2,0,1]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 链表中节点的数目在范围 [0, 500] 内
 * -100 <= Node.val <= 100
 * 0 <= k <= 2 * 10^9
 *
 *
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
// package main

// type ListNode struct {
// 	Val  int
// 	Next *ListNode
// }

func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	l := 0
	cur := head
	for {
		l++
		if cur.Next == nil {
			cur.Next = head
			break
		}
		cur = cur.Next
	}
	step := l - (k % l)
	pre := head
	for i := 0; i < step-1; i++ {
		pre = pre.Next
	}
	tmp := pre.Next
	pre.Next = nil
	return tmp
}

// @lc code=end
