/*
 * @lc app=leetcode.cn id=234 lang=golang
 *
 * [234] 回文链表
 *
 * https://leetcode.cn/problems/palindrome-linked-list/description/
 *
 * algorithms
 * Easy (53.13%)
 * Likes:    1685
 * Dislikes: 0
 * Total Accepted:    587.4K
 * Total Submissions: 1.1M
 * Testcase Example:  '[1,2,2,1]'
 *
 * 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：head = [1,2,2,1]
 * 输出：true
 *
 *
 * 示例 2：
 *
 *
 * 输入：head = [1,2]
 * 输出：false
 *
 *
 *
 *
 * 提示：
 *
 *
 * 链表中节点数目在范围[1, 10^5] 内
 * 0 <= Node.val <= 9
 *
 *
 *
 *
 * 进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
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
func isPalindrome(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return true
	}

	// 取中技巧
	s, f := head, head.Next
	for f != nil && f.Next != nil {
		f = f.Next.Next
		s = s.Next
	}

	cur := s.Next
	s.Next = nil
	var pre *ListNode
	for cur != nil {
		cur.Next, cur, pre = pre, cur.Next, cur
	}
	head2 := pre

	// compare
	c1, c2 := head, head2
	for c1 != nil && c2 != nil {
		if c1.Val != c2.Val {
			return false
		}
		c1 = c1.Next
		c2 = c2.Next
	}
	return true
}

// @lc code=end
