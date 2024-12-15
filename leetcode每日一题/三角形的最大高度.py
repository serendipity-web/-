from linecache import cache


class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        return max(self.calculate(red,blue), self.calculate(blue,red))
    def calculate(self, num1:int,num2:int):
        count=0
        sign = 1
        while True:
            if sign%2==0:
                if (num1-sign)>=0:
                    num1-=sign
                else:
                    break
                count+=1
                sign += 1
            else:
                if (num2-sign)>=0:
                    num2-=sign
                else:
                    break
                count+=1
                sign += 1
        return count



if __name__ == '__main__':
    num1 = 10
    num2 = 1
    print(Solution().maxHeightOfTriangle(num1,num2))
