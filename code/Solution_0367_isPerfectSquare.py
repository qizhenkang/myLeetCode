# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 09:29:52 2021

@author: Zhenkang
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        典型的二分查找 
        
        测试一次出错，二次通过，性能良好
        """
        if num ==1:
            return True
        left = 0
        right = num - 1
        while left < right:
            mid = (left + right)//2
            val = mid ** 2
            # print(left,mid,right)
            if val == num:
                return True
            elif val < num:
                left = mid + 1
            else:
                right = mid
        return False

if __name__ == '__main__':
    solu = Solution()
    heightMap = 2e31
    output_Str = 'result = ' + str(solu.isPerfectSquare(heightMap))
    print(output_Str)