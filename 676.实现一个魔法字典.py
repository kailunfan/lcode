#
# @lc app=leetcode.cn id=676 lang=python
#
# [676] 实现一个魔法字典
#
# https://leetcode-cn.com/problems/implement-magic-dictionary/description/
#
# algorithms
# Medium (55.96%)
# Likes:    43
# Dislikes: 0
# Total Accepted:    2.7K
# Total Submissions: 4.7K
# Testcase Example:  '["MagicDictionary", "buildDict", "search", "search", "search", "search"]\n' +
'[[], [["hello","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]'
#
# 实现一个带有buildDict, 以及 search方法的魔法字典。
#
# 对于buildDict方法，你将被给定一串不重复的单词来构建一个字典。
#
# 对于search方法，你将被给定一个单词，并且判定能否只将这个单词中一个字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。
#
# 示例 1:
#
#
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False
#
#
# 注意:
#
#
# 你可以假设所有输入都是小写字母 a-z。
# 为了便于竞赛，测试所用的数据量很小。你可以在竞赛结束后，考虑更高效的算法。
# 请记住重置MagicDictionary类中声明的类变量，因为静态/类变量会在多个测试用例中保留。 请参阅这里了解更多详情。
#
#
#

# @lc code=start
from collections import defaultdict


class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        def Node(): return defaultdict(Node)
        self.root = Node()

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        self.dict = dict
        for word in dict:
            cur = self.root
            for w in word:
                cur = cur[w]
            cur['#'] = True

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        def f(d, wd, modified):
            if len(wd) == 0 and d.get('#') and modified:
                return True
            for i, s in enumerate(wd):
                # if not d.get(s) and modified:
                #     return False
                for k, v in d.items():
                    if k == '#':
                        continue
                    if modified and k != s:
                        continue
                    if f(v, wd[i + 1:], modified or k != s):
                        return True
                return False

        return f(self.root, word, False)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
# @lc code=end
