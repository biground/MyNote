#
# @lc app=leetcode.cn id=973 lang=python3
#
# [973] 最接近原点的 K 个点
#

# @lc code=start
class Solution:
    def sortRule(self, elem):
        return elem[0]**2 + elem[1]**2
    def kClosest(self, points, K):
        points.sort(key=self.sortRule)
        return points[:K]

# Solution().kClosest([[3,3],[5,-1],[-2,4]], 2)
# @lc code=end

