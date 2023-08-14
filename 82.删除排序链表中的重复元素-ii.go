/*
 * @lc app=leetcode.cn id=82 lang=golang
 *
 * [82] 删除排序链表中的重复元素 II
 *
 * https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/description/
 *
 * algorithms
 * Medium (53.55%)
 * Likes:    1111
 * Dislikes: 0
 * Total Accepted:    336.2K
 * Total Submissions: 627.9K
 * Testcase Example:  '[1,2,3,3,4,4,5]'
 *
 * 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：head = [1,2,3,3,4,4,5]
 * 输出：[1,2,5]
 *
 *
 * 示例 2：
 *
 *
 * 输入：head = [1,1,1,2,3]
 * 输出：[2,3]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 链表中节点数目在范围 [0, 300] 内
 * -100 <= Node.val <= 100
 * 题目数据保证链表已经按升序 排列
 *
 *
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
package main

// 审题出错
// func deleteDuplicates1(head *ListNode) *ListNode {
// 	lc, rc := head, head
// 	for rc != nil {
// 		if lc.Val != rc.Val {
// 			lc.Next = rc
// 			lc = rc
// 		}
// 		rc = rc.Next
// 	}
// 	return head
// }

/*
1. head有可能改变, 需加sentry;
2. 分情况处理,需向后peek一个元素;
*/
func deleteDuplicates(head *ListNode) *ListNode {
	sentry := &ListNode{0, head}
	cur := sentry
	for cur.Next != nil && cur.Next.Next != nil {
		if cur.Next.Val != cur.Next.Next.Val {
			cur = cur.Next
		} else {
			val := cur.Next.Val
			rc := cur.Next
			for rc != nil && rc.Val == val {
				rc = rc.Next
			}
			cur.Next = rc
		}
	}
	return sentry.Next
}

// @lc code=end
