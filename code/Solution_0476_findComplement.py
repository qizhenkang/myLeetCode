# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 09:42:15 2021

@author: qizhe
"""

class Solution:
    def findComplement(self, num: int) -> int:
        """
        读题：
        1、开始还不太会做，知道是位运算
        2、结束条件不容易考虑
        3、本质思想是一位一位拿出来考虑
        
        测试：
        1、一次通过，性能良好
        2、与1009题相同
        
        答案：
        1、用了异或什么的，先找最高位
        """
        result = 0
        i = 0
        while num >0:
            result |= 0 << i if num & 0b1  else 1 << i
            num >>= 1
            i += 1
        
        return result

if __name__ == '__main__':
    solu = Solution()

    # nums = [3,2,1,5]
    n = 8
    # edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
    # time = 3

    result = solu.findComplement(n)

    output_Str = ' result = ' + str(result)
    print(output_Str)