# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 19:33:42 2021

@author: qizhe
"""
from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        读题：
        1、读中文的题目没读懂，对比英文的大概懂了
        2、给定位数n，给编码顺序，编码的特点是相邻只变一位
        3、暴力搜索肯定是可以的，但能不能从逻辑上直接逐个生成呢？
        4、感觉是一种深度优先搜索，但规则好像没有想的特别清楚
        5、感觉是把 00 01 10 11 改成 00 01 11 10 这样的，然后进行组合
        
        测试：
        1、一次通过，30min，性能不好
        
        答案：
        1、答案的意思，也是找了一个规律，镜像 + 添0/1
        2、性能差别不大
        
        答案2：
        1、一行解决，性能可以了，有随机
        """
        return [i ^ (i >> 1)  for i in range(2 ** n)]
        
        # if n == 0:
        #     return [0]
        
        # N = 2**n
        # result = [0] * (N)
        
        # for i in range(n):
        #     for j in range(N):
        #         bitNum = (j // 2 ** i) % 4
        #         if bitNum == 1 or bitNum == 2:
        #             result[j] |= 1 << i
                
        # return result
        
        # if n == 0:
        #     return [0]
        # N = 2**n
        # result = [0] * N
        # # current = 
        # binDict = {0:0b00,
        #            1:0b01,
        #            2:0b11,
        #            3:0b10,
        #            4:0b10,
        #            5:0b11,
        #            6:0b01,
        #            7:0b00}
        # bit = 0
        # # lastFlag = 0
        # while bit < n:
        #     for i in range(N):
        #         print(bit,i,bin(binDict[(i // 2 ** bit) % 8]))
        #         result[i] |= binDict[(i // 2 ** bit) % 8] << bit
        #     bit += 2
        # zeroAndNum = ~(2**(n-1) << bit - 1 )
        # if n % 2:
        #     for i in range(N):
        #         result[i] &= zeroAndNum 

        # return result

if __name__ == '__main__':
    solu = Solution()

    # nums = [3,2,1,5]

    n = 3
    inputList = [1]
    inputList = [2, 1, 5, 6, 2, 3]
    inputList = [2, 2]
    # time = 3
    # beginWord = "ymain"
    # endWord = "oecij"
    # wordList = ["ymann","yycrj","oecij","ymcnj","yzcrj","yycij","xecij","yecij","ymanj","yzcnj","ymain"]
    result = solu.grayCode(n)

    output_Str = ' result = ' + str(result)
    print(output_Str)