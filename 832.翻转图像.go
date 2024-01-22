/*
 * @lc app=leetcode.cn id=832 lang=golang
 *
 * [832] 翻转图像
 *
 * https://leetcode.cn/problems/flipping-an-image/description/
 *
 * algorithms
 * Easy (79.39%)
 * Likes:    310
 * Dislikes: 0
 * Total Accepted:    104.6K
 * Total Submissions: 131.8K
 * Testcase Example:  '[[1,1,0],[1,0,1],[0,0,0]]'
 *
 * 给定一个 n x n 的二进制矩阵 image ，先 水平 翻转图像，然后 反转 图像并返回 结果 。
 *
 * 水平翻转图片就是将图片的每一行都进行翻转，即逆序。
 *
 *
 * 例如，水平翻转 [1,1,0] 的结果是 [0,1,1]。
 *
 *
 * 反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。
 *
 *
 * 例如，反转 [0,1,1] 的结果是 [1,0,0]。
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：image = [[1,1,0],[1,0,1],[0,0,0]]
 * 输出：[[1,0,0],[0,1,0],[1,1,1]]
 * 解释：首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
 * ⁠    然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
 * 输出：[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
 * 解释：首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]；
 * ⁠    然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
 *
 *
 *
 *
 * 提示：
 *
 *
 *
 *
 * n == image.length
 * n == image[i].length
 * 1 <= n <= 20
 * images[i][j] == 0 或 1.
 *
 *
 */
package main

// @lc code=start
func flipAndInvertImage(image [][]int) [][]int {
	l := len(image)
	for _, r := range image {
		i, j := 0, l-1
		for i <= j {
			r[i], r[j] = r[j]^1, r[i]^1
			i++
			j--
		}
	}
	return image
}

// @lc code=end
