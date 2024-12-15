from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        aim_num = []
        nums.sort()
        while len(nums) > 0:
            max_num = nums.pop()
            min_num = nums.pop(0)
            aim_num.append((max_num + min_num) / 2)
        aim_num.sort()
        return aim_num.pop(0)


if __name__ == '__main__':
    s = Solution()
    print(s.minimumAverage(nums = [7,8,3,4,15,13,4,1]))

