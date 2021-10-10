# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:38:32 2021

@author: qizhe
"""

class Solution:
    def minOperations(self, grid, x: int) -> int:
        """
        读题：因为要最小操作数，感觉要求一个平均值，然后再讨论是否可以做到全部一致
        
        1、平均值：遍历
        2、是否全部一致：最小元素差 奇偶数判断，感觉上是一个取余？是不是一个最小差距 然后看是不是能整除x
        
        为什么不给我一个一维的变量呢
        """
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        # gridArray = 
        for i in range(m):
            for j in range(n):
                cnt += grid[i][j]
        average = round(cnt / (m*n))
        
        # 找最接近平均数的一个元素
        # 是不是应该找中位数
        
        aimNumber = grid[0][0]
        gridOne = []
        for i in range(m):
            for j in range(n):
                gridOne.append(grid[i][j])
        gridOne.sort()
        aimNumber = gridOne[(m*n)//2]
        # # print
        # print(gridOne[(m*n)//2])
        # # endFlag = 0
        # for i in range(m):
        #     for j in range(n):
        #         if abs(aimNumber-average) > abs(grid[i][j]-average):
        #             aimNumber = grid[i][j]
                
        #         # if aimNumber == average:
        #         #     endFlag = 1
        #         #     break
                
        #         # if abs(grid[i][j]-average) < x and grid[i][j] > average:
        #         #     # print(grid[i][j],average)
        #         #     aimNumber = grid[i][j]
        #         #     endFlag = 1
        #         #     break
        #     # if endFlag:
        #     #     break
        # if aimNumber > average:
        #     aimNumber2 = aimNumber - x
        # else:
        #     aimNumber2 = aimNumber + x
        # aimNumber = 596 + x
        opeCnt = 0
        for i in range(m):
            for j in range(n):
                if abs(grid[i][j] -aimNumber) % x == 0:
                    opeCnt += abs(grid[i][j] -aimNumber) // x
                    # print(opeCnt1,abs(grid[i][j] -aimNumber) // x,aimNumber)
                else:
                    return -1
                # print(average,aimNumber,opeCnt)
    
        # print(opeCnt1,opeCnt2)
        return opeCnt


if __name__ == '__main__':
    solu = Solution()

    # m = 3
    grid = [[1,2],[3,4]]
    x = 2
    grid = [[1,5],[2,3]]
    x = 1
    grid = [[2,4],[6,8]]
    x = 2
    grid = [[980,476,644,56],[644,140,812,308],[812,812,896,560],[728,476,56,812]]
    x = 84
    
    # grid = [[454,328,160,286,664],[496,538,748,244,286],[34,244,454,706,790],[496,538,832,958,328],[370,874,370,874,286]]
    # x = 42
    # grid = [[596,904,960,232,120,932,176],[372,792,288,848,960,960,764],[652,92,904,120,680,904,120],[372,960,92,680,876,624,904],[176,652,64,344,316,764,316],[820,624,848,596,960,960,372],[708,120,456,92,484,932,540]]
    # x = 28
    result = solu.minOperations(grid, x)
    # output_Str = ' result = '
    # print(' result = ',end=' ')
    # while result:
    #     print(result.val,end=' ')
    #     result = result.next


    output_Str = ' result = ' + str(result) 
    print(output_Str)