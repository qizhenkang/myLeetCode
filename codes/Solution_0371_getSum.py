# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 00:06:55 2021

@author: qizhe
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # result = a + b
        # 答案是要用位运算，和我想的方向一致，但具体操作没见过，不太会
        # 没完全懂
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 2^32
        MASK = 0x100000000
        # 整型最大值
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        while b != 0:
            # 计算进位
            carry = (a & b) << 1 
            # 取余范围限制在 [0, 2^32-1] 范围内
            a = (a ^ b) % MASK
            b = carry % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)   


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    # input_List = [7,1,5,3,6,4]
    # input_List = [2,1,2,0,1]
    # input_int = 6

    result = solu.getSum(-1000,-10)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)