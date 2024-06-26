/*
 * @lc app=leetcode.cn id=147 lang=golang
 *
 * [147] 对链表进行插入排序
 *
 * https://leetcode.cn/problems/insertion-sort-list/description/
 *
 * algorithms
 * Medium (69.46%)
 * Likes:    611
 * Dislikes: 0
 * Total Accepted:    146.8K
 * Total Submissions: 211.4K
 * Testcase Example:  '[4,2,1,3]'
 *
 * 给定单个链表的头 head ，使用 插入排序 对链表进行排序，并返回 排序后链表的头 。
 *
 * 插入排序 算法的步骤:
 *
 *
 * 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
 * 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
 * 重复直到所有输入数据插入完为止。
 *
 *
 *
 * 下面是插入排序算法的一个图形示例。部分排序的列表(黑色)最初只包含列表中的第一个元素。每次迭代时，从输入数据中删除一个元素(红色)，并就地插入已排序的列表中。
 *
 * 对链表进行插入排序。
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 *
 *
 * 输入: head = [4,2,1,3]
 * 输出: [1,2,3,4]
 *
 * 示例 2：
 *
 *
 *
 *
 * 输入: head = [-1,5,3,4,0]
 * 输出: [-1,0,3,4,5]
 *
 *
 *
 * 提示：
 *
 *
 *
 *
 * 列表中的节点数在 [1, 5000]范围内
 * -5000 <= Node.val <= 5000
 *
 *
 */
package main

import "fmt"

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

func printLinkList(head *ListNode) {
	for head != nil {
		fmt.Printf("%d->", head.Val)
		head = head.Next
	}
	fmt.Printf("nil\n")
}

func insertionSortList1(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}

	sentry := &ListNode{-5001, head}
	cur := head
	for cur.Next != nil {
		if cur.Next.Val > cur.Val {
			cur = cur.Next
		} else {
			lc := sentry
			for lc.Next.Val < cur.Next.Val {
				lc = lc.Next
			}
			lc.Next, cur.Next, cur.Next.Next = cur.Next, cur.Next.Next, lc.Next
		}
	}
	return sentry.Next
}

// @lc code=end
