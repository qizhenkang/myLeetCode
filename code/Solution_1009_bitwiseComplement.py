# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 09:52:24 2021

@author: qizhe
"""

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        """
        与476题同样，测试样例多了一个0
        """
        if n == 0:
            return 1
        result = 0
        i = 0
        while n >0:
            result |= 0 << i if n & 0b1  else 1 << i
            n >>= 1
            i += 1
        
        return result