# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 17:15:32 2021

@author: qizhe
"""

class Solution:
    def solveNQueens(self, n: int):
        """
        典型的回溯问题
        读题目，他要的是，所有解，不是找到一个就可以
        """
        
        def dfs(n,result,current,num,validPositionStack):
            
            if num == n:
                result.append(current)
                return
            
            # for i in range(num,n*n):
            #     # print(i,result)
            #     if validPosition[i//n][i % n]:
                    
            #         for k in range(n*n):
            #             if k == i//n or k == i%n or (abs(i - k) % (n-1)) == 0 or (abs(i - k) % (n+1)) == 0:
            #                 validPosition[k//n][k % n] = False
            # dfs(n,result,current+[i],num+1,validPosition)
                    # break
            return
        
        result = []
        current = []
        validPositionStack = [[True]*n for _ in range(n)] 
        dfs(n,result,current,0,validPositionStack)
        
        # for start in range(1,n-1):
        #     validPosition
        #     for i in range(n):
        #         for j in range(n):
        #             if validPosition[i][j]:
        #                 current += [i*n+j]
                    
        
        return result

if __name__ == '__main__':
    solu = Solution()
    
    input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    input_List = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    # input_List = 1

    result = solu.solveNQueens(4)

    output_Str = ' result = ' + str(result)
    print(output_Str)
