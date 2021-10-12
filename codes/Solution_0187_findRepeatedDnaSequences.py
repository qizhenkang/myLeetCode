# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 00:05:44 2021

@author: qizhe
"""

class Solution:
    def findRepeatedDnaSequences(self, s: str):
        """
        读题：
        1、感觉像是，在找一个重复字符串，同时字符串长度为10，不是找目标，而是没有目标地找
        2、心理上感觉比较麻烦，没有想到好办法
        3、长度固定为10，字符只有ATCG四种，字符串最长达到1e5
        4、感觉是一个长度固定为10的滑动窗口，然后做一个哈希表来计数，不确定是否会超时
        
        测试：
        1、错误一次，通过，但效率不是很高
        2、用时10min
        
        答案：
        1、答案利用了ATCG进行了位运算的优化，本质上是利用滑动窗口每次只改变1点点
        2、这里的做法：1 ATCG映射为 00 01 10 11； 2 利用滑动窗口
        
        改后效果：
        1、测试通过，用时81% 内存90%
        """
        N = len(s)
        if N <= 10:
            return []
        result = []
        ATCGdict = {'A':0b00,'T':0b01,'C':0b10,'G':0b11}
        window = int(0)
        strDict = {}
        for i in range(10):
            window <<= 2
            window |= ATCGdict[s[i]]
        strDict[window] = 1
        # print(window)
        for i in range(10,N):
            # print(i,'1',bin(window))
            window <<= 2
            window |= ATCGdict[s[i]]
            window &= 1048575
            # print(i,'2',bin(window))
            if window in strDict:
                strDict[window] += 1
                if s[i-9:i+1] not in result:
                    result.append(s[i-9:i+1])
            else:
                strDict[window] =1
        # print(strDict)
        return result
        
        
        
        
if __name__ == '__main__':
    solu = Solution()
    
    # input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    # input_List = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    # s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    s = "AAAAAAAAAAAAA"
    # intervals = [[1,1],[3,5],[6,7],[8,10],[12,16]]
    # newInterval = [2,17]
    # intervals = [[2,5]]
    # newInterval = [5,7]
    # input_List = 1
    # numerator = -50
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    result = solu.findRepeatedDnaSequences(s)

    output_Str = ' result = ' + str(result) 
    print(output_Str)