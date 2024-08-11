'''
大小为 n x n 的矩阵 grid 中有一条蛇。蛇可以朝 四个可能的方向 移动。矩阵中的每个单元格都使用位置进行标识： grid[i][j] = (i * n) + j。
蛇从单元格 0 开始，并遵循一系列命令移动。
给你一个整数 n 表示 grid 的大小，另给你一个字符串数组 commands，其中包括 "UP"、"RIGHT"、"DOWN" 和 "LEFT"。题目测评数据保证蛇在整个移动过程中将始终位于 grid 边界内。
返回执行 commands 后蛇所停留的最终单元格的位置
'''
from typing import List

'''
思路: 感觉比较偏数学一点，对应的东南西北有对数字的对应计算，按照计算即可
假设当前位置为x,向右: x+1，向左:x-1,向上:x+n,向下x-n
UP:
RIGHT:
DOWN:
LEFT:
'''


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        num = 0
        for str_x in commands:
            if str_x == "LEFT":
                num -= 1
            elif str_x == "RIGHT":
                num += 1
            elif str_x == "UP":
                num -= n
            elif str_x == "DOWN":
                num += n
            else:
                raise Exception(f"illegal str is {str_x}")
        return num


if __name__ == '__main__':
    x = 3
    commands = ["DOWN","RIGHT","UP"]
    solution = Solution()
    print(solution.finalPositionOfSnake(x, commands))
