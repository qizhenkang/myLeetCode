# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 10:10:03 2021

@author: qizhe
"""

class Solution:
    def numberToWords(self, num: int) -> str:
        """
        感觉位运算好一点
        """
        numDict = { 0:'Zero',
                    1:'One' ,
                    2:'Two',
                    3:'Three',
                    4:'Four',
                    5:'Five',
                    6:'Six',
                    7:'Seven',
                    8:'Eight',
                    9:'Nine',
                    10:'Ten',
                    11:'Eleven',
                    12:'Twelve',
                    13:'Thirteen',
                    14:'Fourteen',
                    15:'Fifteen',
                    16:'Sixteen',
                    17:'Seventeen',
                    18:'Eighteen',
                    19:'Nineteen',
                    20:'Twenty',
                    30:'Thirty',
                    40:'Forty',
                    50:'Fifty',
                    60:'Sixty',
                    70:'Seventy',
                    80:'Eighty',
                    90:'Ninety',
                    100:'Hundred',
                    1000:'Thousand',
                    1001:'Million',
                    1002:'Billion'
                    # 104:'Trillion'
                    }
        N = len(str(num))
        numstr = str(num)
        numstr = numstr[::-1]
        nums = [ int(i) for i in numstr]
        
        pointer = N-1
        bit = 0
        result = ''
        useFlag = 0
        nonzeroFlag = 1
        while pointer>=0:
            bit = pointer % 3
            # if bit == 3:
            #     result += numDict[nums[pointer]]+ ' ' + numDict[1000]+ ' '
            if bit == 2:
                if nums[pointer] != 0:
                    result += numDict[nums[pointer]]+ ' ' + numDict[100]+ ' '
                    nonzeroFlag = 1
            elif bit == 1:
                # print(n,pointer,nums,nums[pointer])
                if nums[pointer] >=2:
                    result += numDict[nums[pointer]*10]+ ' '
                    nonzeroFlag = 1
                elif nums[pointer] ==1:
                    result += numDict[int(numstr[pointer]+numstr[pointer-1])]+ ' ' 
                    # pointer -=1 # 相当于-2
                    useFlag = 1
                    nonzeroFlag = 1
            else:
                if not (N > 1 and nums[pointer] == 0) and not useFlag:
                    result += numDict[nums[pointer]]+ ' '
                    nonzeroFlag = 1
                if useFlag:    
                    useFlag = 0
                if nonzeroFlag:
                    if (pointer+1) // 3 == 3:
                        result += numDict[1002]+ ' '
                    elif (pointer+1) // 3 == 2:
                        result += numDict[1001]+ ' '
                    elif (pointer+1) // 3 == 1:
                        result += numDict[1000]+ ' '
                    nonzeroFlag = 0

            pointer -=1
        
        return result[:-1]
        
        

if __name__ == '__main__':
    solu = Solution()
    lists = [ 1234567891]
    for n in lists:
        # n = 1
        result = solu.numberToWords(n)
    
    
    
        output_Str = ' result = ' + str(result) 
        print(output_Str)