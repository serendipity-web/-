'''
对应链接: https://leetcode.cn/problems/determine-color-of-a-chessboard-square/
问题类型：逻辑推理
时间复杂度L O(n)
空间复杂度
'''


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        '''

        :param coordinates: example: a1 ,b
        :way 计算偶数 or 奇数来判断结果
        :return:
        '''
        change_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        return (change_dict[coordinates[0]] + int(coordinates[1])) % 2 == 1

if __name__ == '__main__':
    print(ord('a'))