#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (26.52%)
# Likes:    2302
# Dislikes: 0
# Total Accepted:    259.5K
# Total Submissions: 921.1K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？请你找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
# 示例：
#
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#

# @lc code=start


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        L = len(nums)
        for i in range(L):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, L):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                # for k in range(j+1, L):
                #     if k>j+1 and nums[k] == nums[k-1]:
                #         continue
                #     this_ans = [nums[i], nums[j], nums[k]]
                #     if sum(this_ans) == 0:
                #         ans.append(this_ans)
            
                # 优化第三层循环,从右向左,知道和小于0
                target = -(nums[i] + nums[j])
                k = L-1
                while nums[k] > target and k>j:
                    k -= 1
                if j == k:
                    break
                if nums[k] == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    
        return ans


# Solution().threeSum([-1,0,1,2,-1,-4])
# @lc code=end
