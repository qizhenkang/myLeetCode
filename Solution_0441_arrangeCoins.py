# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 09:32:50 2021

@author: qizhe
"""
import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        读题：
        1、感觉上是一个求和嘛，就想了一个数学的办法
        
        
        答案：
        1、二分查找
        2、直接数学算法：我想的稍微麻烦了一点，差一点就直接到正确答案了
        """
        
        # 答案思路1：二分查找
        # 这里的 mid left right的处理很巧 没懂他的核心思想
        
        # left = 1
        # right = n
        # while left < right:
        #     mid = (left+right+1)//2
        #     print(left,mid,right)
            
        #     if mid *(mid+1) <= 2*n:
        #         left = mid
        #     else:
        #         right = mid -1
        # return left
        
        # 答案思路2：直接数学
        
        return int((-1+math.sqrt(1+8*n) )/2)
        

        # 我的思路：
        # Start = int(-1+math.sqrt(1+2*n))
        # End = math.ceil(math.sqrt(2*n))
        # # print(Start,End)
        # result = -1
        # for i in range(Start,End+1):
        #     if 2 * n <= i**2 + i:
        #         if 2*n == i**2 + i:
        #             result = i
        #         else:
        #             result = i-1
        #         break

        
        # return result

        

if __name__ == '__main__':
    solu = Solution()

    # m = 3
    n = 991
    result = solu.arrangeCoins(n)
    # output_Str = ' result = '
    # print(' result = ',end=' ')
    # while result:
    #     print(result.val,end=' ')
    #     result = result.next


    output_Str = ' result = ' + str(result) 
    print(output_Str)