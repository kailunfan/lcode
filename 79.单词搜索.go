/*
 * @lc app=leetcode.cn id=79 lang=golang
 *
 * [79] 单词搜索
 */
package main

import "fmt"

// @lc code=start

type pair struct{ x, y int }

var directions = []pair{{-1, 0}, {1, 0}, {0, -1}, {0, 1}} // 上下左右

func exist(board [][]byte, word string) bool {
	h, w := len(board), len(board[0])
	vis := make([][]bool, h)
	for i := range vis {
		vis[i] = make([]bool, w)
	}

	// 考察word第k位
	var check func(i, j, k int) bool
	check = func(i, j, k int) bool {
		// 单词不匹配
		if board[i][j] != word[k] {
			return false
		}
		// 单词存在于网格中
		if k == len(word)-1 {
			return true
		}
		vis[i][j] = true
		// 回溯时还原已访问的单元格
		for _, dir := range directions {
			if newI, newJ := i+dir.x, j+dir.y; 0 <= newI && newI < h && 0 <= newJ && newJ < w && !vis[newI][newJ] {
				if check(newI, newJ, k+1) {
					return true
				}
			}
		}
		vis[i][j] = false
		return false
	}

	for i, row := range board {
		for j := range row {
			if check(i, j, 0) {
				return true
			}
		}
	}
	return false
}

func exist2(board [][]byte, word string) bool {
	directions := [][]int{{1, 0}, {0, 1}, {-1, 0}, {0, -1}}
	l_x := len(board)
	l_y := len(board[0])

	// 初始化mark
	mark := make([][]int, l_x)
	for i := 0; i < l_x; i++ {
		mark[i] = make([]int, l_y)
	}

	var backTrack func(i, j int, word string) bool
	backTrack = func(i, j int, word string) bool {
		if word == "" {
			return true
		}
		for _, d := range directions {
			cur_i := i + d[0]
			cur_j := j + d[1]
			if cur_i > 0 && cur_i < l_x && cur_j > 0 && cur_j < l_y && board[cur_i][cur_j] == word[0] {
				if mark[cur_i][cur_j] == 1 {
					continue
				}
				mark[cur_i][cur_j] = 1
				if backTrack(cur_i, cur_j, word[1:]) == true {
					return true
				} else {
					mark[cur_i][cur_j] = 0
				}
			}
		}
		return false
	}

	for i := 0; i < l_x; i++ {
		for j := 0; j < l_y; j++ {
			if board[i][j] == word[0] {
				mark[i][j] = 1
				if backTrack(i, j, word[1:]) == true {
					return true
				} else {
					mark[i][j] = 0
				}
			}
		}
	}
	return false
}

// @lc code=end

type Item struct {
	x    int
	y    int
	val  string
	seen []string
}

func exist1(board [][]byte, word string) bool {
	// 初始元素
	max_y := len(board[0]) - 1
	max_x := len(board) - 1
	word_len := len(word)
	for i := 0; i <= max_x; i++ {
		for j := 0; j <= max_y; j++ {
			if board[i][j] == word[0] {
				if string(board[i][j]) == word {
					return true
				}
				ans := []Item{{i, j, string(board[i][j]), []string{fmt.Sprintf("%d%d", i, j)}}}
				for len(ans) != 0 {
					new_ans := []Item{}
					for _, a := range ans {
						if len(a.val) >= word_len {
							continue
						}
						for _, action := range [][]int{{1, 0}, {0, 1}, {-1, 0}, {0, -1}} {
							x := a.x + action[0]
							y := a.y + action[1]
							if x > max_x || y > max_y || x < 0 || y < 0 {
								continue
							}
							hasSeen := false
							for _, s := range a.seen {
								if s == fmt.Sprintf("%d%d", x, y) {
									hasSeen = true
									break
								}
							}
							if hasSeen {
								continue
							}
							new_val := a.val + string(board[x][y])
							if new_val == word {
								return true
							}
							seen := append([]string{fmt.Sprintf("%d%d", x, y)}, a.seen...)
							new_ans = append(new_ans, Item{x, y, new_val, seen})
						}
					}
					ans = new_ans
				}
			}
		}
	}

	return false
}
