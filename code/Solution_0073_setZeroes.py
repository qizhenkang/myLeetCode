# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 22:42:55 2021

@author: qizhe
"""

class Solution:
    def setZeroes(self, matrix) -> None:
        """
        读题：
        第一反应就是用两个list，记录需要的行/列
        测试：
        通过
        
        答案：
        要求用O(1)的算法：
        思想是，利用行/列的第一个元素，作为list
        
        测试：
        通过
        """
        # zeroRow = []
        # zeroCol = []
        
        
        m = len(matrix)
        n = len(matrix[0])
        firstRowFlag = any(matrix[0][j] == 0 for j in range(n))
        firstColFlag = any(matrix[i][0] == 0 for i in range(m))
        
        
        for i in range(m-1,0,-1):
            for j in range(n-1,0,-1):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,m):
            if matrix[i][0] == 0:    
                matrix[i] = [0]*n
        
        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        if firstRowFlag:
            matrix[0] = [0]*n
        if firstColFlag:
            for i in range(m):
                matrix[i][0] = 0
        
        return matrix
        
        

if __name__ == '__main__':
    solu = Solution()
    
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    # matrix = [[1,1,1],[1,0,1],[1,1,1]]
    # input_List = 1

    result = solu.setZeroes(matrix)

    output_Str = ' result = ' + str(result)
    print(output_Str)