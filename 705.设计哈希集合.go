/*
* @lc app=leetcode.cn id=705 lang=golang
*
* [705] 设计哈希集合
*
* https://leetcode.cn/problems/design-hashset/description/
*
  - algorithms
  - Easy (63.40%)
  - Likes:    318
  - Dislikes: 0
  - Total Accepted:    109K
  - Total Submissions: 171.8K
  - Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n' +
    '[[],[1],[2],[1],[3],[2],[2],[2],[2]]'

*
* 不使用任何内建的哈希表库设计一个哈希集合（HashSet）。
*
* 实现 MyHashSet 类：
*
*
* void add(key) 向哈希集合中插入值 key 。
* bool contains(key) 返回哈希集合中是否存在这个值 key 。
* void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
*
*
*
* 示例：
*
*
* 输入：
* ["MyHashSet", "add", "add", "contains", "contains", "add", "contains",
* "remove", "contains"]
* [[], [1], [2], [1], [3], [2], [2], [2], [2]]
* 输出：
* [null, null, null, true, false, null, true, null, false]
*
* 解释：
* MyHashSet myHashSet = new MyHashSet();
* myHashSet.add(1);      // set = [1]
* myHashSet.add(2);      // set = [1, 2]
* myHashSet.contains(1); // 返回 True
* myHashSet.contains(3); // 返回 False ，（未找到）
* myHashSet.add(2);      // set = [1, 2]
* myHashSet.contains(2); // 返回 True
* myHashSet.remove(2);   // set = [1]
* myHashSet.contains(2); // 返回 False ，（已移除）
*
*
*
* 提示：
*
*
* 0 <= key <= 10^6
* 最多调用 10^4 次 add、remove 和 contains
*
*
*/
package main

// @lc code=start
type MyHashSet struct {
	value map[int]struct{}
}

func Constructor() MyHashSet {
	return MyHashSet{map[int]struct{}{}}
}

func (this *MyHashSet) Add(key int) {
	this.value[key] = struct{}{}
}

func (this *MyHashSet) Remove(key int) {
	delete(this.value, key)
}

func (this *MyHashSet) Contains(key int) bool {
	if _, ok := this.value[key]; ok {
		return true
	}
	return false
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(key);
 * obj.Remove(key);
 * param_3 := obj.Contains(key);
 */
// @lc code=end
