"""
记录学生出勤次数
满足True的条件：1. ’A‘的次数小于2 2.连续’L‘的次数小于3
"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        # 判断false coordination1
        if s.count('A') >= 2:
            return False
        if s.find("LLL") != -1:
            return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkRecord("PPALLP"))
