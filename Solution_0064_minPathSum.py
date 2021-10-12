# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 20:48:08 2021

@author: qizhe
"""

class Solution:
    def minPathSum(self, grid) -> int:
        """
        读完题，好像有一个所谓的迪杰斯特拉算法，但我好像不会
        我回溯试试吧
        
        回溯不剪枝 怕是要超时
        
        测试：
        1、回溯确实超时
        2、是不是有所谓的前缀和，搞一个优先队列
        
        不会做，看答案：
        1、典型DP问题
        
        测试：
        1、dp未优化空间，用时66% 内存30%
        2、想到优化的思路，用时86% 内存97%
        
        """
        m = len(grid)
        n = len(grid[0])
        
        # 优化dp ，从 m*n矩阵 变成 1*n矩阵
        dp = [0]*n
        dp[0] = grid[0][0]
        for j in range(1,n):
            dp[j] = dp[j-1] + grid[0][j]
            
        for i in range(1,m):
            for j in range(n):
                if j==0:
                    dp[0] += grid[i][0]
                else:
                    dp[j] = min(dp[j-1],dp[j]) + grid[i][j]

        return dp[n-1]
            
        
        # dp = [[0]*n for _ in range(m)]
        
        # dp[0][0] = grid[0][0]
        # for j in range(1,n):
        #     dp[0][j] = dp[0][j-1] + grid[0][j]
        # for i in range(1,m):
        #     dp[i][0] = dp[i-1][0] + grid[i][0]
        
        # for i in range(1,m):
        #     for j in range(1,n):
        #         dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        
        # return dp[m-1][n-1]
        
        
        # def dfs(grid,current,i,j,m,n):
            
        #     print(i,j)
        #     if i >= m or j >=n:
        #         return current + 10000
        #     if i==m-1 and j ==n-1:
        #         return current + grid[i][j]
            
        #     return min(dfs(grid,current + grid[i][j],i+1,j,m,n),dfs(grid,current+ grid[i][j],i,j+1,m,n))
        # m = len(grid)
        # n = len(grid[0])
        # # result = 0
        # # current = 0
        
        # return dfs(grid,0,0,0,m,n)

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
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    # grid = [[1,2,3],[4,5,6]]
    # n = 1
    result = solu.minPathSum(grid)
    # output_Str = ' result = '
    # print(' result = ',end=' ')
    # while result:
    #     print(result.val,end=' ')
    #     result = result.next


    output_Str = ' result = ' + str(result) 
    print(output_Str)