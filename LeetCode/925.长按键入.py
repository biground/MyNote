#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        length = len(name)
        typedLen = len(typed)
        if length > typedLen:
            return False
        nameStart = 0
        typedStart = 0

        while(typedStart < typedLen):
            if nameStart < length and typed[typedStart] == name[nameStart]:
                nameStart += 1
                typedStart += 1
            elif nameStart > 0 and typed[typedStart] == name[nameStart - 1]:
                typedStart += 1
            else:
                return False
        
        if nameStart < length:
            return False
                
        return True

Solution().isLongPressedName("zlexya", "aazlllllllllllllleexxxxxxxxxxxxxxxya")
# @lc code=end

