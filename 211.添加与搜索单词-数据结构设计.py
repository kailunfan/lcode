#
# @lc app=leetcode.cn id=211 lang=python
#
# [211] 添加与搜索单词 - 数据结构设计
#
# https://leetcode-cn.com/problems/add-and-search-word-data-structure-design/description/
#
# algorithms
# Medium (44.03%)
# Likes:    125
# Dislikes: 0
# Total Accepted:    11.5K
# Total Submissions: 25.7K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' +
'[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# 设计一个支持以下两种操作的数据结构：
#
# void addWord(word)
# bool search(word)
#
#
# search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。
#
# 示例:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
#
#
# 说明:
#
# 你可以假设所有单词都是由小写字母 a-z 组成的。
#
#

# @lc code=start


from collections import defaultdict


class WordDictionary:

    def __init__(self):
        self.d = {}  # 字典树

    def addWord(self, word):
        cur = self.d  # 单词填进字典树
        for c in word:
            if not cur.get(c):
                cur[c] = {}
            cur = cur[c]
        cur['#'] = True

    # def search(self,word):
    #     state = [self.d]
    #     for i,c in enumerate(word):
    #         temp_state = []
    #         for s in state:
    #             if not isinstance(s,defaultdict):
    #                 continue
    #             if c in s.keys():
    #                 temp_state.append(s[c])
    #             elif c ==".":
    #                 temp_state.extend(s.values())

    #         state = temp_state
    #     for s in state:
    #         if isinstance(s,defaultdict) and '#' in s:
    #             return True

    #     return False

    def search(self, word):
        "广度优先搜索"
        candicates = [self.d]
        for w in word:
            tmp = []
            if w == ".":
                has_match = False
                for can in candicates:
                    if [x for x in can.keys() if x != "#"]:
                        has_match = True
                        tmp.extend([v for k, v in can.items() if k != "#"])
                if not has_match:
                    return False
            else:
                has_match = False
                for can in candicates:
                    if can.get(w):
                        has_match = True
                        tmp.append(can.get(w))
                if not has_match:
                    return False
            candicates = tmp
        return any(['#' in i for i in candicates])

    def search2(self, word):
        "深搜"
        def s(node, wd):
            cur = node
            for ind, w in enumerate(wd):
                if w == ".":
                    return any([s(v, wd[ind+1:]) for k, v in cur.items() if k != "#"])
                cur = cur.get(w)
                if not cur:
                    return False
            return cur.get('#', False)

        return s(self.d, word)

    def search1(self, word):
        "深度优先搜索+剪枝"
        self.cut = False

        def f(td, s):  # 深搜，参数为：当前子字典，当前串
            if self.cut:  # 剪枝
                return True
            cur = td
            for i, c in enumerate(s):
                if c == '.':
                    return any(f(cur[key], s[i + 1:]) for key in cur if key != '#')
                cur = cur.get(c)
                if not cur:
                    return False
            ans = cur.get('#') is not None
            if ans:
                self.cut = True
            return ans
        return f(self.d, word)


w = WordDictionary()
for i in ["a"]:
    w.addWord(i)
print(w.search("a."))

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
