# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 10:04:50 2021

@author: qizhe
"""

class Solution:
    def toHex(self, num: int) -> str:
        result = ''
        hexDict = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        if num == 0:
            return '0'
        if num < 0:
            num = 16**8 + num
        while num > 0:
            result = hexDict[num % 16] + result
            num //= 16

        return result
        
        
        
        
        
        
        
if __name__ == '__main__':
    solu = Solution()
    
    input_List = [1,6,5,4,3,2,1]
    
    # input_List = 1

    result = solu.toHex(-4096)

    output_Str = ' result = ' + str(result)
    print(output_Str)