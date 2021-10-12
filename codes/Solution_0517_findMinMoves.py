# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 10:47:10 2021

@author: qizhe
"""

class Solution:
    def findMinMoves(self, machines) -> int:
        
        """
        看的答案，不是很懂，用了一个所谓的前缀和
        """
        
        N = len(machines)
        total = sum(machines)
        if total % N:
            return -1
        Aim = total // N
        
        num = 0
        prevSum = 0
        result = 0
        for x in machines:
            num = x - Aim
            prevSum += num
            result = max(result,num,abs(prevSum)) 
        
        
        return result
        
        

if __name__ == '__main__':
    solu = Solution()

    input_List = [1,0,5] # 3
    # input_List = [0,3,0] # 2

    result = solu.findMinMoves(input_List)

    output_Str = 'result = ' + str(result)
    print(output_Str)