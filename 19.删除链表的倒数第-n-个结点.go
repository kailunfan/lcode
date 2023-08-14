/*
 * @lc app=leetcode.cn id=19 lang=golang
 *
 * [19] 删除链表的倒数第 N 个结点
 *
 * https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/
 *
 * algorithms
 * Medium (45.37%)
 * Likes:    2517
 * Dislikes: 0
 * Total Accepted:    1.1M
 * Total Submissions: 2.5M
 * Testcase Example:  '[1,2,3,4,5]\n2'
 *
 * 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：head = [1,2,3,4,5], n = 2
 * 输出：[1,2,3,5]
 *
 *
 * 示例 2：
 *
 *
 * 输入：head = [1], n = 1
 * 输出：[]
 *
 *
 * 示例 3：
 *
 *
 * 输入：head = [1,2], n = 1
 * 输出：[1]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 链表中结点的数目为 sz
 * 1 <= sz <= 30
 * 0 <= Node.val <= 100
 * 1 <= n <= sz
 *
 *
 *
 *
 * 进阶：你能尝试使用一趟扫描实现吗？
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


func removeNthFromEnd(head *ListNode, n int) *ListNode {
	/*
		双指针
		1. 开始位置
		2. 结束条件
		3. 推进步骤
	*/
	sentry := &ListNode{0, head}
	lc, rc := sentry, head
	for i := 0; i < n; i++ {
		rc = rc.Next
	}
	for rc != nil {
		lc = lc.Next
		rc = rc.Next
	}
	lc.Next = lc.Next.Next
	return sentry.Next
}

// @lc code=end
