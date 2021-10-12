# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 15:17:51 2021

@author: qizhe
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int: 
        """
        读题：
        1、这题以前做过，但因为超时过去了
        2、超时的原因是顺序查找了，能不能想办法2分查找呢，不就做出来了么
        3、其实就是找，a是b的 几倍，
            
        测试
        1、起点是什么呢？是不是应该有一个自适应的过程，否则很慢
        
        通过了，但抄的答案，还不是很懂，有一个自适应的迭代过程
        """

        def div(A,B): 
            # print(A,B)
            if A < B:
                # print(A,'<',B)
                return 0
            sumx = B
            result = 1
            while True:
                if sumx < A:
                    # 自适应加倍
                    sumx <<= 1
                    result <<= 1
                elif sumx == A:
                    return result
                else:
                    sumx >>= 1
                    result >>= 1
                    return result + div( A - sumx, B)
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend == INT_MIN:
                return INT_MAX
            else:
                return -dividend
        sign = 1
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            sign = -1
            
        result = div(abs(dividend),abs(divisor))
        
        if sign >0:
            return result if result < INT_MAX else INT_MAX
            
        return -result
            
            
        
        
        
        

        # sumx = 0
        # result = 0
        # if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
        #     sumx -= abs(divisor)
        #     while -sumx <= abs(dividend):
        #         sumx -= abs(divisor)
        #         result -= 1
        # else:
        #     sumx += abs(divisor)
        #     while sumx <= abs(dividend):
        #         sumx += abs(divisor)
        #         result += 1
        
        # return result

if __name__ == '__main__':
    solu = Solution()
    
    # input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    # input_List = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    # intervals = "Hello, my name is John"
    # n5 = ListNode(5)
    # n4 = ListNode(4,n5)
    # n3 = ListNode(3,n4)
    # n2 = ListNode(2,n3)
    # n1 = ListNode(1,n2)
    # n0 = ListNode(0,n1)
    # k = 2
    # input_List = 1
    # numerator = -50
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # grid = [[1,3,1],[1,5,1],[4,2,1]]
    # grid = [[1,2,3],[4,5,6]]
    # n = 1
    result = solu.divide(2**31,1)
    # output_Str = ' result = '
    # print(' result = ',end=' ')
    # while result:
    #     print(result.val,end=' ')
    #     result = result.next


    output_Str = ' result = ' + str(result) 
    print(output_Str)