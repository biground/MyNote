#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        result = dict()
        process = dict()
        for i in arr:
            if i not in process:
                process[i] = 0
            process[i] += 1
        for k, v in process.items():
            if v in result:
                return False
            result[v] = k
        return True
# @lc code=end
