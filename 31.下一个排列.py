#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# https://leetcode-cn.com/problems/next-permutation/description/
#
# algorithms
# Medium (33.17%)
# Likes:    596
# Dislikes: 0
# Total Accepted:    79.3K
# Total Submissions: 231.3K
# Testcase Example:  '[1,2,3]'
#
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#
#

# @lc code=start


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 从后向前找到打破降序规则的元素
        # 从降序序列中找到最小的比该元素大的进行交换
        # 然后反转降序部分
        l = len(nums)
        for i in range(l-1, 0, -1):
            if nums[i-1] < nums[i]:
                c = l-1
                while nums[c] <= nums[i-1]:
                    c -= 1
                nums[i-1], nums[c] = nums[c], nums[i-1]
                break
        else:
            i = 0

        # 反转i,l-1后半部分
        lc, rc = i, l-1
        while lc < rc:
            nums[lc], nums[rc] = nums[rc], nums[lc]
            lc += 1
            rc -= 1

# @lc code=end
