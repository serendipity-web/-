from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans.append(self.check_value(num))
        return ans


    def check_value(self,y):
        if y & (y + 1) == 0:
            return y - 1
        return -1

if __name__ == '__main__':
    nums = [11,13,31]
    print(Solution().minBitwiseArray(nums))
