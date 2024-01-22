/*
 * @lc app=leetcode.cn id=876 lang=golang
 *
 * [876] 链表的中间结点
 *
 * https://leetcode.cn/problems/middle-of-the-linked-list/description/
 *
 * algorithms
 * Easy (70.55%)
 * Likes:    970
 * Dislikes: 0
 * Total Accepted:    433.5K
 * Total Submissions: 614.1K
 * Testcase Example:  '[1,2,3,4,5]'
 *
 * 给你单链表的头结点 head ，请你找出并返回链表的中间结点。
 *
 * 如果有两个中间结点，则返回第二个中间结点。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：head = [1,2,3,4,5]
 * 输出：[3,4,5]
 * 解释：链表只有一个中间结点，值为 3 。
 *
 *
 * 示例 2：
 *
 *
 * 输入：head = [1,2,3,4,5,6]
 * 输出：[4,5,6]
 * 解释：该链表有两个中间结点，值分别为 3 和 4 ，返回第二个结点。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 链表的结点数范围是 [1, 100]
 * 1 <= Node.val <= 100
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
func middleNode(head *ListNode) *ListNode {
	l, r := head, head
	for r != nil && r.Next != nil {
		l = l.Next
		r = r.Next.Next
	}
	return l
}

// @lc code=end
