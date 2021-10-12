# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 19:23:46 2021

@author: qizhe
"""

import math
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        """
        读题：
        1、和上一题的区别，就是增加了障碍物
        2、我有点感觉，还是可以用组合数学来做
        3、好像不这么简单，你再试试
        
        不会做了，看答案
        
        答案：
        动态规划
        """
        def uniquePath(m,n):
            return round(math.factorial(m + n - 2) / math.factorial(n-1) / math.factorial(m-1))
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        result = uniquePath(m, n)
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    # pass
                    result -= uniquePath(m-i, n-j) * uniquePath(i+1, j+1)
                    # print(i,j,result,uniquePath(m-i, n-j),uniquePath(i+1, j+1))

        return result
        # return comb(m + n - 2, n - 1)

        # if m > n:
        #     m, n=n, m
        
        # result = 1
        
        # for x in range(n,m + n - 1):
        #     result *=x
        
        # for x in range(1,m):
        #     result /=x
        
        # return round(result)

        # return round(math.factorial(m + n - 2) / math.factorial(n-1) / math.factorial(m-1))
        
        # def dfs(i,j,m,n):
        #     if i == m-1 and j == n-1:
        #         return 1
        #     if i >= m or j >=n:
        #         return 0
            
        #     return dfs(i+1, j, m, n) + dfs(i, j+1, m, n)
        
        # return dfs(0,0,m,n)

if __name__ == '__main__':
    solu = Solution()
    
    # input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    # input_List = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    # intervals = "Hello, my name is John"
    # n5 = ListNode(5)
    # n4 = ListNode(4,n5)
    # n3 = ListNode(3,n4)
    # n2 = ListNode(2,n3)
    # n1 = ListNode(1,n2)
    # n0 = ListNode(0,n1)
    # k = 2
    # input_List = 1
    # numerator = -50
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    obstacleGrid = [[0,1,0],[0,1,0],[0,0,0]]
    # obstacleGrid = [[0,1],[0,0]]
    result = solu.uniquePathsWithObstacles(obstacleGrid)
    # output_Str = ' result = '
    # print(' result = ',end=' ')
    # while result:
    #     print(result.val,end=' ')
    #     result = result.next


    output_Str = ' result = ' + str(result) 
    print(output_Str)