/*
 * @lc app=leetcode.cn id=24 lang=golang
 *
 * [24] 两两交换链表中的节点
 *
 * https://leetcode.cn/problems/swap-nodes-in-pairs/description/
 *
 * algorithms
 * Medium (71.28%)
 * Likes:    1782
 * Dislikes: 0
 * Total Accepted:    608.3K
 * Total Submissions: 853.3K
 * Testcase Example:  '[1,2,3,4]'
 *
 * 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：head = [1,2,3,4]
 * 输出：[2,1,4,3]
 *
 *
 * 示例 2：
 *
 *
 * 输入：head = []
 * 输出：[]
 *
 *
 * 示例 3：
 *
 *
 * 输入：head = [1]
 * 输出：[1]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 链表中节点的数目在范围 [0, 100] 内
 * 0 <= Node.val <= 100
 *
 *
 */

package main

type ListNode struct {
	Val  int
	Next *ListNode
}

/**
* Definition for singly-linked list.
* type ListNode struct {
	*     Val int
	*     Next *ListNode
	* }
*/

// @lc code=start
func swapPairs(head *ListNode) *ListNode {
	// 迭代
	sentry := &ListNode{0, head}
	cur := sentry
	for cur != nil && cur.Next != nil && cur.Next.Next != nil {
		cur, cur.Next, cur.Next.Next, cur.Next.Next.Next = cur.Next, cur.Next.Next, cur.Next.Next.Next, cur.Next
	}
	return sentry.Next
}

func swapPairs1(head *ListNode) *ListNode {
	// 递归
	if head == nil || head.Next == nil {
		return head
	}
	tmp := head.Next
	head.Next, head.Next.Next = swapPairs(head.Next.Next), head
	return tmp
}

// @lc code=end
