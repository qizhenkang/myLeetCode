# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 11:14:56 2021

@author: qizhe
"""

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """
        第一反应感觉循环不太好处理，偷看了一眼答案，需要“小学除法”，大概有思路了
        
        """
        minus = '-' if numerator * denominator < 0 else ''
        numerator = abs(numerator)
        denominator = abs(denominator)
        result = minus + str(numerator // denominator)

        if numerator % denominator:
            result += '.'
        # else:
        #     return result
        
        numerator = 10 * (numerator % denominator)
        
        print(result,numerator)
        
        bit = 0
        quotient = 0
        numeratorCycle = []
        quotientCycle = []
        Decimal = ''
        while numerator and bit < 1e4:
            if numerator > denominator:
                quotient = numerator // denominator
                numerator -= quotient * denominator
            else:
                quotient = 0

            print(numerator,denominator,quotient,numeratorCycle,quotientCycle,Decimal)
            if numerator in numeratorCycle:
                posi = numeratorCycle.index(numerator)
                print(posi)
                if quotientCycle[posi] == quotient:
                    Decimal = Decimal[:posi] +'('+ Decimal[posi:] + ')'
                else:
                    posi +=1
                    Decimal += str(quotient)
                    Decimal = Decimal[:posi] +'('+ Decimal[posi:] + ')'
                break
            numeratorCycle.append(numerator)
            quotientCycle.append(quotient)
            Decimal += str(quotient)
            numerator *= 10
            bit += 1
        
        return result+Decimal
        
        
        
        
if __name__ == '__main__':
    solu = Solution()
    
    input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    input_List = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    # input_List = 1
    numerator = -50
    denominator = 8
    
    result = solu.fractionToDecimal(numerator,denominator)

    output_Str = ' result = ' + str(result) + ' ' + str(numerator/denominator)
    print(output_Str)