#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (52.15%)
# Likes:    1655
# Dislikes: 0
# Total Accepted:    148.1K
# Total Submissions: 281.5K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
#
# 示例:
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
#
#

# @lc code=start
from typing import List


class Solution:
    def trap1(self, height: List[int]) -> int:
        # 模拟
        ans = 0
        for i in range(1, len(height)-1):
            left_max, right_max = 0, 0
            for lc in range(0, i):
                if height[lc] > left_max:
                    left_max = height[lc]
            for rc in range(i+1, len(height)):
                if height[rc] > right_max:
                    right_max = height[rc]

            this_ans = min(left_max, right_max)
            if this_ans > height[i]:
                ans += this_ans-height[i]

        return ans

    def trap2(self, height: List[int]) -> int:
        # 动态规划求每个位置两边最大高度
        left_max, right_max = [0]*len(height), [0]*len(height)
        left_max[0] = height[0]
        right_max[-1] = height[-1]

        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i])

        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        ans = 0
        for i in range(1, len(height)-1):
            m = min(left_max[i-1], right_max[i+1])
            if m > height[i]:
                ans += m-height[i]
        return ans

    def trap(self, height: List[int]) -> int:
        # 双指针
        ans = 0 
        left, right = 0,len(height)-1
        left_max,right_max = 0,0
        while left<right:
            left_max = max(left_max,height[left])
            right_max = max(right_max,height[right])
            if height[left]<height[right]:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max-height[right]
                right -= 1
        return ans


# @lc code=end
