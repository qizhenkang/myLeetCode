# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 10:30:57 2021

@author: qizhe
"""

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        numFlag = 0
        numlist = ['0','1','2','3','4','5','6','7','8','9']
        num = 0
        numseq = []
        for i in s:
            # print(i,numseq)
            if i in numlist:
                numFlag = 1
                num = 10 * num + int(i)
            else:
                if numFlag:
                    if not numseq:
                        numseq.append(num)
                    elif numseq[-1]<num:
                        numseq.append(num)
                    else:
                        return False
                numFlag = 0
                num = 0
        if numFlag:
            if not numseq:
                numseq.append(num)
            elif numseq[-1]<num:
                numseq.append(num)
            else:
                return False
            
        
        return True
        
if __name__ == '__main__':
    solu = Solution()
    
    input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    input_List = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    # input_List = 1
    s = "hello world 5 x 5"
    result = solu.areNumbersAscending(s)

    output_Str = ' result = ' + str(result)
    print(output_Str)