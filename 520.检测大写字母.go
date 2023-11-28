/*
 * @lc app=leetcode.cn id=520 lang=golang
 *
 * [520] 检测大写字母
 *
 * https://leetcode.cn/problems/detect-capital/description/
 *
 * algorithms
 * Easy (56.75%)
 * Likes:    253
 * Dislikes: 0
 * Total Accepted:    91.5K
 * Total Submissions: 161.5K
 * Testcase Example:  '"USA"'
 *
 * 我们定义，在以下情况时，单词的大写用法是正确的：
 *
 *
 * 全部字母都是大写，比如 "USA" 。
 * 单词中所有字母都不是大写，比如 "leetcode" 。
 * 如果单词不只含有一个字母，只有首字母大写， 比如 "Google" 。
 *
 *
 * 给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：word = "USA"
 * 输出：true
 *
 *
 * 示例 2：
 *
 *
 * 输入：word = "FlaG"
 * 输出：false
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= word.length <= 100
 * word 由小写和大写英文字母组成
 *
 *
 */
package main

// @lc code=start
func detectCapitalUse(word string) bool {
	if len(word) <= 1 {
		return true
	}
	if (word[0] >= 'a' && word[1] <= 'a') {
		return false
	}
	for i := 2; i < len(word); i++ {
		if (word[1] >= 'a' && word[i] < 'a') || (word[1] < 'a' && word[i] >= 'a') {
			return false
		}
	}
	return true
}

// @lc code=end
