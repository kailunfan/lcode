/*
 * @lc app=leetcode.cn id=17 lang=golang
 *
 * [17] 电话号码的字母组合
 *
 * https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/
 *
 * algorithms
 * Medium (58.08%)
 * Likes:    2500
 * Dislikes: 0
 * Total Accepted:    707.1K
 * Total Submissions: 1.2M
 * Testcase Example:  '"23"'
 *
 * 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
 *
 * 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：digits = "23"
 * 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
 *
 *
 * 示例 2：
 *
 *
 * 输入：digits = ""
 * 输出：[]
 *
 *
 * 示例 3：
 *
 *
 * 输入：digits = "2"
 * 输出：["a","b","c"]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= digits.length <= 4
 * digits[i] 是范围 ['2', '9'] 的一个数字。
 *
 *
 */
package main


func letterCombinations1(digits string) []string {
	if digits == "" {
		return []string{}
	}
	keyMap := map[string]string{
		"2": "abc",
		"3": "def",
		"4": "ghi",
		"5": "jkl",
		"6": "mno",
		"7": "pqrs",
		"8": "tuv",
		"9": "wxyz",
	}
	ans := []string{}
	var backTrack func(ind int, tmp string)
	backTrack = func(ind int, tmp string) {
		if ind == len(digits) {
			ans = append(ans, tmp)
		} else {
			for _, l := range keyMap[string(digits[ind])] {
				backTrack(ind+1, tmp+string(l))
			}
		}
	}
	backTrack(0, "")
	return ans
}

// iter 
// @lc code=start
func letterCombinations(digits string) []string {
	if len(digits) == 0 {
		return []string{}
	}

	numToLetters := map[byte]string{
		'2': "abc",
		'3': "def",
		'4': "ghi",
		'5': "jkl",
		'6': "mno",
		'7': "pqrs",
		'8': "tuv",
		'9': "wxyz",
	}

	res := []string{""}
	for i := 0; i < len(digits); i++ {
		letters := numToLetters[digits[i]]
		thisRes := []string{}
		for _, r := range res {
			for _, l := range letters {
				thisRes = append(thisRes, r+string(l))
			}
		}
		res = thisRes
	}
	return res
}
// @lc code=end
