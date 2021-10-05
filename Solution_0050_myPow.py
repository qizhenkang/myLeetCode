# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 13:56:04 2021

@author: qizhe
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        读题：这题一开始看，不知道要考什么，顺手写了一串代码，处理了一下0和n<0的特殊情况
        测试：提交了3次，出了各种错误，发现这题不那么简单
        放弃继续
        看答案：
        1、此题考什么呢？要求你进行快速计算，比如n他会输入2**31-1的大小，直接计算是不可能的
        2、比如 x**77 那你需要 一个一个地乘77次吗，显然不合适
        方案一：递归思路
        可以算x **76 * x = (x** 38)**2 * x = x** 19 ** 2 ** 2 * x ……
        所以 只需要计算中间过程为：
        [1,x,x2,x4,x9,x19,x38,x77]
        
        方案二：迭代思路
        77 = '0b1001101' = 64 + 8 +4 + 1 = 77
        
        """
        if x == 0:
            return 0
        
        if n < 0:
            x = 1/x
            n = -n
        
        result = 1
        # xnow = x
        while n > 0:
            if n % 2:
                result *= x
            x *= x
            n //=2
        return result
            
        
        # if x == 0:
        #     return 0
        
        # if n < 0:
        #     x = 1/x
        #     n = -n
        
        # result = 1
        # resultPrev = 1
        # while n>0:
        #     result *= x

        #     if abs(result - resultPrev) < 1e-12 or abs(result) > 1e4:
        #         break
        #     n -=1
        #     resultPrev = result
            
        return result
        

if __name__ == '__main__':
    solu = Solution()
    
    input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    input_List = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    # input_List = 1
    numerator = -50
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    result = solu.myPow(2,77)
    


    output_Str = ' result = ' + str(result) 
    print(output_Str)