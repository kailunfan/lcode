#
# @lc app=leetcode.cn id=835 lang=python
#
# [835] 图像重叠
#
# https://leetcode-cn.com/problems/image-overlap/description/
#
# algorithms
# Medium (57.83%)
# Likes:    33
# Dislikes: 0
# Total Accepted:    2.2K
# Total Submissions: 3.8K
# Testcase Example:  '[[1,1,0],[0,1,0],[0,1,0]]\n[[0,0,0],[0,1,1],[0,0,1]]'
#
# 给出两个图像 A 和 B ，A 和 B 为大小相同的二维正方形矩阵。（并且为二进制矩阵，只包含0和1）。
# 
# 我们转换其中一个图像，向左，右，上，或下滑动任何数量的单位，并把它放在另一个图像的上面。之后，该转换的重叠是指两个图像都具有 1 的位置的数目。
# 
# （请注意，转换不包括向任何方向旋转。）
# 
# 最大可能的重叠是什么？
# 
# 示例 1:
# 
# 输入：A = [[1,1,0],
# ⁠         [0,1,0],
# [0,1,0]]
# B = [[0,0,0],
# [0,1,1],
# [0,0,1]]
# 输出：3
# 解释: 将 A 向右移动一个单位，然后向下移动一个单位。
# 
# 注意: 
# 
# 
# 1 <= A.length = A[0].length = B.length = B[0].length <= 30
# 0 <= A[i][j], B[i][j] <= 1
# 
# 
#

# @lc code=start
from collections import Counter

class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        # 在A中定位每个为1的单元格,尝试所有偏移量,如果B也为1,counts[偏移] += 1
        counts = Counter()
        for i,row in enumerate(A):
            for j,col in enumerate(row):
                if not col:
                    continue
                for i1,row1 in enumerate(B):
                    for j1,col1 in enumerate(row1):
                        if not col1:
                            continue
                        counts[i-i1,j-j1] += 1
        return max(counts.values() or [0])
                      
        
# @lc code=end

