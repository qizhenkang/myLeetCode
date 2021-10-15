# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:32:36 2021

@author: qizhe
"""

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        """
        读题：
        1、第一眼反应：做两次二分查找就可以结束了
        2、仔细一想：是不是完全可以做一次二分查找就可以呢？
        2、数据量是100*100，感觉不难
        
        测试：
        1、一次通过了，但边界条件不太行
        """
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = m*n-1
        # print(matrix[0][0])
        # if matrix[0][0] == target or matrix[m-1][n-1] == target:
        #     return True
        while left <= right:
            mid = (right+ left)//2 
            print(left,mid,right)
            x = matrix[mid // n][mid % n]
            if x < target:
                left = mid + 1
            elif x > target:
                right = mid -1
            else:
                return True
        
        return False
        
        

if __name__ == '__main__':
    solu = Solution()
    
    word1 = "horse"
    
    word2 = 'ros'
    # arr = '/home//foo/'
    # arr = '/../'
    # matrix = [[1,1,1],[1,0,1],[1,1,1]]
    # input_List = 1
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3

    result = solu.searchMatrix(matrix,target)

    output_Str = ' result = ' + str(result)
    print(output_Str)