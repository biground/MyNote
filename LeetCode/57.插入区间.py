#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
# [1,4],[3,7],[5,8]
# [6,7] [1,4]
# @lc code=start
class Solution:
    def insert(self, intervals, newInterval):
        start = newInterval[0]

        for i in range(len(intervals)):
            if intervals[i][0] > start:
                intervals.insert(i, newInterval)
                newInterval = None
                break
        if newInterval:
            intervals.append(newInterval)
        curIndex = 0
        cur = intervals[curIndex]
        while cur:
            nowStart, nowEnd = cur
            nextStart, nextEnd = intervals[curIndex + 1] if len(intervals) > curIndex + 1 else (None, None)
            # 尝试向后合并
            if nextStart is not None and nextEnd is not None and nextStart <= nowEnd and nextEnd >= nowStart:
                intervals[curIndex] = [min(nextStart, nowStart), max(nextEnd, nowEnd)]
                intervals.pop(curIndex + 1)
                curIndex -= 1
            curIndex += 1
            cur = intervals[curIndex] if len(intervals) > curIndex else None

        return intervals

# Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
# Solution().insert([[1,3],[6,9]], [2,5])
Solution().insert([[0,4],[0,5]], [7,12])
# @lc code=end

