'''
给你两个整数数组 nums1 和 nums2，长度分别为 n 和 m。同时给你一个正整数 k
如果 nums1[i] 可以被 nums2[j] * k 整除，则称数对 (i, j) 为 优质数对（0 <= i <= n - 1, 0 <= j <= m - 1）。
返回 优质数对 的总数。
'''
from typing import List, Counter


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count = Counter(nums1)
        max1 = max(count)
        res = 0
        for a, cnt in Counter(nums2).items():
            for b in range(a * k, max1 + 1, a * k):
                if b in count:
                    res += count[b] * cnt
        return res


if __name__ == '__main__':
    nums1 = [1, 2, 4, 12]
    nums2 = [2, 4]
    k = 3
    print(Solution().numberOfPairs(nums1, nums2, k))
