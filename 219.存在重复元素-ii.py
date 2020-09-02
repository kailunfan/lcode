#
# @lc app=leetcode.cn id=219 lang=python
#
# [219] 存在重复元素 II
#
# https://leetcode-cn.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (38.29%)
# Likes:    178
# Dislikes: 0
# Total Accepted:    49K
# Total Submissions: 124.9K
# Testcase Example:  '[1,2,3,1]\n3'
#
# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的
# 绝对值 至多为 k。
# 
# 
# 
# 示例 1:
# 
# 输入: nums = [1,2,3,1], k = 3
# 输出: true
# 
# 示例 2:
# 
# 输入: nums = [1,0,1,1], k = 1
# 输出: true
# 
# 示例 3:
# 
# 输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false
# 
#

# @lc code=start
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 暴力,超时
        # L = len(nums)
        # for i in range(L):
        #     for j in range(i+1,i+k+1):
        #         if j<L and nums[i] == nums[j]:``
        #             return True
        # return False

        # 也是暴力
        # st = []
        # for i in nums:
        #     if i in st:
        #         return True
        #     st.append(i)
        #     if len(st) > k:
        #         st.pop(0)
        # return False

        # set
        st = {}
        for i in range(len(nums)):
            if nums[i] in st and i - st[nums[i]] <= k:
                return True
            st[nums[i]] = i
        return False



# @lc code=end

