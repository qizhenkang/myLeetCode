# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 13:39:19 2021

@author: qizhe
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        纯原创做法，实际上重点考虑了 不同长度/进位处理
        """
        carry = 0
        a = list(a)
        b = list(b)
        stack = []
        while a or b or carry:
            # 获取当前位 / 若无则为0
            abit = int(a.pop()) if a else 0
            bbit = int(b.pop()) if b else 0
            # 计算加法
            newbit = abit + bbit + carry
            # 计算进位/当前位
            carry = newbit // 2
            newbit %= 2
            
            stack.append(str(newbit))
        
        return ''.join(stack[::-1])
        
        
if __name__ == '__main__':
    solu = Solution()
    
    str1 = '11'
    str2 = '1'
    result = solu.addBinary(str1,str2)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)