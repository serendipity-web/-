from typing import List

#
# class Solution:
#     def duplicateNumbersXOR(self, nums: List[int]) -> int:
#         eum_dict = {}
#         aim_num = []
#         for num in nums:
#             eum_dict[num] = 0
#         for num in nums:
#             eum_dict[num] += 1
#             if eum_dict[num] == 2:
#                 aim_num.append(num)
#         endnum = 0
#         for num in aim_num:
#             endnum ^= num
#         return endnum

from collections import Counter


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        num_count = Counter(nums)  # 计算每个数字出现的次数
        result = 0
        print(num_count)

        for num, count in num_count.items():
            if count == 2:
                result ^= num  # 出现两次的数字进行 XOR 操作

        return result





if __name__ == '__main__':
    nums1 = [1,3, 2, 2,1]

    # 实例化 Solution
    solution = Solution()

    # 调用实例方法
    print(solution.duplicateNumbersXOR(nums1))
