# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 16:29:55 2021

@author: qizhe
"""

class Solution:
    def rotate(self, matrix) -> None:
        """
        做了半小时这题，就是一个替换。
        这里用了一点优化，就是每4个同时替换
        """
        N = len(matrix)
        GroupNumber = 4
        for i in range(N):
            for j in range(i,N-i-1):
                # print(i,j,'->',j,N-1-i)
                # print(matrix[i][j],'->',matrix[j][N-1-i])
                tempi = i
                tempj = j
                tempvalLast = matrix[tempi][tempj]
                for x in range(GroupNumber):
                    # print(tempi,tempj)
                    tempval = matrix[tempj][N - 1 - tempi]
                    matrix[tempj][N - 1 - tempi] = tempvalLast
                    
                    tempvalLast = tempval
                    tempi, tempj = tempj, N - 1 - tempi

        #         print(matrix)
        
        # return matrix
                



if __name__ == '__main__':
    solu = Solution()
    
    input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    input_List = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    # input_List = 1

    result = solu.rotate(input_List)

    output_Str = ' result = ' + str(result)
    print(output_Str)