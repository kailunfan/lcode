#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (58.08%)
# Likes:    312
# Dislikes: 0
# Total Accepted:    63.1K
# Total Submissions: 107K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
# 
# 示例:
# 
# 输入: [1,1,2]
# 输出:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
#

# @lc code=start
import copy

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        result = []
        visited = [False] * len(nums)
        def backtrack(tmp):
            if len(tmp) == len(nums):
                result.append(tmp)
                return 
            for i in range(len(nums)):
                if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                    continue
                visited[i] = True
                backtrack(tmp + [nums[i]])
                visited[i] = False
            return result
        return backtrack([])

        
        ans = []
        l = len(nums)

        def search(value,used_index):
            if len(value) == l and value not in ans:
                ans.append(value[:])
            for i in range(l):
                if i not in used_index:
                    value.append(nums[i])
                    used_index.append(i)
                    search(value,used_index)
                    value.pop()
                    used_index.pop()
        search([],[])
        return ans
# @lc code=end

