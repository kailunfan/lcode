#
# @lc app=leetcode.cn id=838 lang=python
#
# [838] 推多米诺
#
# https://leetcode-cn.com/problems/push-dominoes/description/
#
# algorithms
# Medium (44.53%)
# Likes:    55
# Dislikes: 0
# Total Accepted:    3.4K
# Total Submissions: 7.5K
# Testcase Example:  '".L.R...LR..L.."'
#
# 一行中有 N 张多米诺骨牌，我们将每张多米诺骨牌垂直竖立。
#
# 在开始时，我们同时把一些多米诺骨牌向左或向右推。
#
#
#
# 每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。
#
# 同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。
#
# 如果同时有多米诺骨牌落在一张垂直竖立的多米诺骨牌的两边，由于受力平衡， 该骨牌仍然保持不变。
#
# 就这个问题而言，我们会认为正在下降的多米诺骨牌不会对其它正在下降或已经下降的多米诺骨牌施加额外的力。
#
# 给定表示初始状态的字符串 "S" 。如果第 i 张多米诺骨牌被推向左边，则 S[i] = 'L'；如果第 i 张多米诺骨牌被推向右边，则 S[i] =
# 'R'；如果第 i 张多米诺骨牌没有被推动，则 S[i] = '.'。
#
# 返回表示最终状态的字符串。
#
# 示例 1：
#
# 输入：".L.R...LR..L.."
# 输出："LL.RR.LLRRLL.."
#
# 示例 2：
#
# 输入："RR.L"
# 输出："RR.L"
# 说明：第一张多米诺骨牌没有给第二张施加额外的力。
#
# 提示：
#
#
# 0 <= N <= 10^5
# 表示多米诺骨牌状态的字符串只含有 'L'，'R'; 以及 '.';
#
#
#

# @lc code=start
import copy


class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        # 验算法
        # l = len(dominoes)
        # lst = [i for i in dominoes]
        # move = True
        # while move:
        #     cp = copy.deepcopy(lst)
        #     move = False
        #     for i, item in enumerate(cp):
        #         if item != '.':
        #             continue
        #         left = cp[i-1] if i-1 >= 0 else None
        #         right = cp[i+1] if i+1 < l else None
        #         if left == "R" and right == "L":
        #             continue
        #         if left == "R":
        #             lst[i] = "R"
        #             move = True
        #         elif right == "L":
        #             lst[i] = "L"
        #             move = True
        # return ''.join(lst)

        # 双指针分组
        lst = [i for i in dominoes]
        # 哨兵
        lst.insert(0, 'L')
        lst.append('R')
        lc = 0
        while True:
            rc = lc + 1
            if rc >= len(lst):
                break
            while lst[rc] == '.':
                rc += 1
            if lst[lc] == lst[rc]:
                for i in range(lc+1, rc):
                    lst[i] = lst[rc]
            elif lst[lc] == 'R' and lst[rc] == 'L':
                lt = lc + 1
                rt = rc - 1
                while lt < rt:
                    lst[lt] = 'R'
                    lst[rt] = 'L'
                    lt += 1
                    rt -= 1
            # 移动指针
            lc = rc
        return ''.join(lst[1:-1])


# @lc code=end
