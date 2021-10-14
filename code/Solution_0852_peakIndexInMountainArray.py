# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 09:37:34 2021

@author: qizhe
"""

class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        """
        读题：
        1、本质上是一个凸函数找最值的问题
        2、梯度下降法 + 二分查找
        
        测试：
        1、5min通过
        
        答案：
        不需要比较两次，只需要两段有不同的特性就可以了，也就是上升还是下降就足够了
        """
        N = len(arr)
        left = 0
        right = N-1
        while left < right:
            mid = (left + right) // 2
            if arr[mid-1] < arr[mid] < arr[mid+1]:
                left = mid
            elif arr[mid-1] > arr[mid] > arr[mid+1]:
                right = mid
            else:
                return mid
        
        
        return mid



if __name__ == '__main__':
    solu = Solution()
    
    arr = [0,10,2]
    # matrix = [[1,1,1],[1,0,1],[1,1,1]]
    # input_List = 1

    result = solu.peakIndexInMountainArray(arr)

    output_Str = ' result = ' + str(result)
    print(output_Str)