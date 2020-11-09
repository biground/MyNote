#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#

# @lc code=start
class Solution:
    def validMountainArray(self, A) -> bool:
        if not A:
            return False
        length = len(A)
        if length < 3:
            return False
        
        # 上升flag
        upFlag = None
        lastNum = A[0]

        for i in range(1, length):
            num = A[i]
            if num == lastNum:
                return False
            if upFlag is None:
                # 初始化
                if num > lastNum:
                    upFlag = True
                    lastNum = num
                    continue
                else:
                    return False
            elif upFlag:
                # 上升情况
                if num < lastNum:
                    upFlag = False
                    lastNum = num
                    continue
            else:
                # 下降情况
                if num > lastNum:
                    return False
            lastNum = num

        return not upFlag

Solution().validMountainArray([0,1,2,3,4,5,6,7,8,9])
# @lc code=end

