# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 20:02:20 2021

@author: qizhe
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        """
        用时10min，就两个循环
        """
        result = '1'
        for i in range(2,n+1):
            cnt = 0
            currentNum = ''
            newresult = ''
            for j in range(len(result)):
                if result[j] == currentNum:
                    cnt += 1
                elif currentNum:
                    newresult += str(cnt) + str(currentNum)
                    currentNum = result[j]
                    cnt = 1
                else:
                    currentNum = result[j]
                    cnt = 1
            newresult += str(cnt) + str(currentNum)
            
            result = newresult
        
        return result
        
if __name__ == '__main__':
    solu = Solution()
    
    # input_List = [1,6,5,4,3,2,1]
    
    input_List = 1

    result = solu.countAndSay(input_List)

    output_Str = ' result = ' + str(result)
    print(output_Str)