# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:57:07 2021

@author: qizhe
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        读题：
        1、通过了不高，然后看了内容，肯定是有一些极端测试例子，所以这个不要急着测试，一定要完善测试例子
        2、非常像那个IP地址的题，典型的回溯
        
        测试：
        1、15min写完，样例都通过了，结果超时了，不通过
        2、那么就需要剪枝
        3、他要的好像只是种类，应该是动态规划吧？只需要连乘就可以了
        4、吃了个饭，好像想出来了优化DP方法
        5、多次测试失败，终于成功了 性能还不好
        
        答案：
        1、真的是，动态规划，他们写的代码好简单啊
        2、思路差不多，答案的思路更清楚一些
        
        """
        # def __dfs(s,begin,length):
        #     if begin == length:
        #         return 1
        #     result = 0
        #     for i in range(begin,min(length,begin + 2)):
        #         if 1 <= int(s[begin:i+1]) <= 26 and s[begin] !='0':
        #             result += __dfs(s,i+1,length)
        #     return result
        # return __dfs(s,0,len(s))
        dplast = 1
        dpnow = 1
        N = len(s)
        if int(s[0]) == 0:
            return 0 
        i = 0
        while i < N:
            # print(s,i,dplast,dpnow)
            if i > 0 and 1 <= int(s[i-1:i+1]) <= 26 and int(s[i-1]) and int(s[i]):
                # 10-26的考虑范围
                dpnow,dplast = dplast + dpnow,dpnow
            elif int(s[i-1]) == 0 and (i-1 == 0 or int(s[i-2]) == 0 or int(s[i-2])>2 or int(s[i]) == 0):
                # 出现单个0，不合法，直接return 0 
                # 00 - 09 的非法情况，这个0必须和前面的配对，否则失败
                dpnow = 0
                break
            elif int(s[i]) == 0 and (int(s[i-1]) == 0 or int(s[i-1])>2):
                # 非法情况 30 40 50 60
                dpnow = 0
                break
            elif int(s[i]) == 0:
                dpnow,dplast = dplast,dplast
            elif i >0 and int(s[i-1:i+1]) > 26:
                # 处理 > 26 的合法情况
                dpnow,dplast = dpnow,dpnow
            i += 1

        return dpnow
        
if __name__ == '__main__':
    solu = Solution()

    # nums = [3,2,1,5]

    n = 8
    inputList = [1]
    inputList = [2, 0, 5, 6, 2, 3]
    matrix = [["0","1","0","1","0"],["1","1","0","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    matrix = []
    matrix = [["0"],['1']]
    matrix = [["1","0"]]
    ss = ['12',"23",'20310','06','011106','111111111111111111111111111111111111111111111']
    ss = ['1234','2101','123123']
    for s in ss:
        result = solu.numDecodings(s)
    
        output_Str = ' result = ' + str(result)
        print(output_Str)
    