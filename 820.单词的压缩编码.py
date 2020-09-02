#
# @lc app=leetcode.cn id=820 lang=python
#
# [820] 单词的压缩编码
#
# https://leetcode-cn.com/problems/short-encoding-of-words/description/
#
# algorithms
# Medium (48.52%)
# Likes:    169
# Dislikes: 0
# Total Accepted:    36.7K
# Total Submissions: 75K
# Testcase Example:  '["time", "me", "bell"]'
#
# 给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。
#
# 例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0,
# 2, 5]。
#
# 对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。
#
# 那么成功对给定单词列表进行编码的最小字符串长度是多少呢？
#
#
#
# 示例：
#
# 输入: words = ["time", "me", "bell"]
# 输出: 10
# 说明: S = "time#bell#" ， indexes = [0, 2, 5] 。
#
#
#
#
# 提示：
#
#
# 1 <= words.length <= 2000
# 1 <= words[i].length <= 7
# 每个单词都是小写字母 。
#
#
#
from collections import defaultdict

# @lc code=start


class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        class Trie:
            def __init__(self):
                def Node(): return defaultdict(Node)
                self.root = Node()

            def insert(self, word):
                cur = self.root
                for w in word[::-1]:
                    cur = cur[w]

            def count(self):
                # 统计节点个数
                ans, depth = 0, 0
                layer = [self.root]
                while layer:
                    depth += 1
                    new_layer = []
                    for node in layer:
                        if len(node) == 0:
                            ans += depth
                            continue
                        else:
                            for item in node.values():
                                new_layer.append(item)
                    layer = new_layer
                return ans

        t = Trie()
        words = list(set(words))
        for word in words:
            t.insert(word)

        return t.count()


# @lc code=end
