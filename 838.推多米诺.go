/*
 * @lc app=leetcode.cn id=838 lang=golang
 *
 * [838] 推多米诺
 *
 * https://leetcode.cn/problems/push-dominoes/description/
 *
 * algorithms
 * Medium (55.75%)
 * Likes:    320
 * Dislikes: 0
 * Total Accepted:    40.4K
 * Total Submissions: 72.6K
 * Testcase Example:  '"RR.L"'
 *
 * n 张多米诺骨牌排成一行，将每张多米诺骨牌垂直竖立。在开始时，同时把一些多米诺骨牌向左或向右推。
 *
 * 每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。
 *
 * 如果一张垂直竖立的多米诺骨牌的两侧同时有多米诺骨牌倒下时，由于受力平衡， 该骨牌仍然保持不变。
 *
 * 就这个问题而言，我们会认为一张正在倒下的多米诺骨牌不会对其它正在倒下或已经倒下的多米诺骨牌施加额外的力。
 *
 * 给你一个字符串 dominoes 表示这一行多米诺骨牌的初始状态，其中：
 *
 *
 * dominoes[i] = 'L'，表示第 i 张多米诺骨牌被推向左侧，
 * dominoes[i] = 'R'，表示第 i 张多米诺骨牌被推向右侧，
 * dominoes[i] = '.'，表示没有推动第 i 张多米诺骨牌。
 *
 *
 * 返回表示最终状态的字符串。
 *
 *
 * 示例 1：
 *
 *
 * 输入：dominoes = "RR.L"
 * 输出："RR.L"
 * 解释：第一张多米诺骨牌没有给第二张施加额外的力。
 *
 *
 * 示例 2：
 *
 *
 * 输入：dominoes = ".L.R...LR..L.."
 * 输出："LL.RR.LLRRLL.."
 *
 *
 *
 *
 * 提示：
 *
 *
 * n == dominoes.length
 * 1 <= n <= 10^5
 * dominoes[i] 为 'L'、'R' 或 '.'
 *
 *
 */
package main

// @lc code=start
func pushDominoes(dominoes string) string {
	s := []byte("L" + dominoes + "R")
	lc := 0
	n := len(s)
	for lc < n-1 {
		rc := lc + 1
		for rc < n && s[rc] == '.' {
			rc++
		}
		if s[rc] == s[lc] {
			for i := lc + 1; i < rc; i++ {
				s[i] = s[rc]
			}
		} else if s[lc] == 'L' && s[rc] == 'R' {
			for i := lc + 1; i < rc; i++ {
				s[i] = '.'
			}
		} else if s[lc] == 'R' && s[rc] == 'L' {
			i, j := lc+1, rc-1
			for ; i < j; i, j = i+1, j-1 {
				s[i] = 'R'
				s[j] = 'L'
			}
			if i == j {
				s[i] = '.'
			}
		}
		lc = rc
	}
	return string(s[1 : len(s)-1])
}

// @lc code=end
