/*
 * @lc app=leetcode.cn id=771 lang=golang
 *
 * [771] 宝石与石头
 *
 * https://leetcode.cn/problems/jewels-and-stones/description/
 *
 * algorithms
 * Easy (85.60%)
 * Likes:    801
 * Dislikes: 0
 * Total Accepted:    213.6K
 * Total Submissions: 249.5K
 * Testcase Example:  '"aA"\n"aAAbbbb"'
 *
 *  给你一个字符串 jewels 代表石头中宝石的类型，另有一个字符串 stones 代表你拥有的石头。 stones
 * 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
 *
 * 字母区分大小写，因此 "a" 和 "A" 是不同类型的石头。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：jewels = "aA", stones = "aAAbbbb"
 * 输出：3
 *
 *
 * 示例 2：
 *
 *
 * 输入：jewels = "z", stones = "ZZ"
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= jewels.length, stones.length <= 50
 * jewels 和 stones 仅由英文字母组成
 * jewels 中的所有字符都是 唯一的
 *
 *
 */
package main

// @lc code=start
func numJewelsInStones(jewels string, stones string) int {
	m := map[rune]bool{}
	for _, v := range jewels {
		m[v] = true
	}
	ans := 0
	for _, v := range stones {
		if m[v] {
			ans++
		}
	}
	return ans
}

// @lc code=end
