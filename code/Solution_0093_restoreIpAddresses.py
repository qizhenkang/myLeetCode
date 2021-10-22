# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 11:48:24 2021

@author: qizhe
"""
from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        读题：
        1、感觉就是一个回溯，放三个点，组成有效IP地址
        
        测试：
        1、一次通过，25min，性能极好
        
        答案：
        1、回溯，思路一致
        """
        def __dfs(s,result,current,begin,length,dotNum):
            # print(current)
            if begin >= length or dotNum > 3:
                return
            if dotNum == 3:
                result.append(current+s[begin:])
                return
            
            for i in range(begin,min(length,begin + 3)):
                # 符合要求的数字是 0 - 256 且首位不能为零 首位为零只有0可以
                if 0 <= int(s[begin:i+1]) < 256 and (s[begin] != '0' or begin == i):
                    if dotNum < 2:
                        __dfs(s,result,current + s[begin:i+1] + '.',i+1,length,dotNum+1)
                    else:
                        # print(i+1,s[i+1:] )
                        # 如果到最后一个点了，那么点之后的最后一个数字也应该符合条件
                        if i+1 < length and (0 <= int(s[i+1:]) < 256 and ( s[i+1] != '0'  or i+1 == length-1) ):
                            __dfs(s,result,current + s[begin:i+1] + '.',i+1,length,dotNum+1)
                else:
                    # 不符合直接退出，说明这种情况没意义了，大幅度剪枝
                    break
            return
            
        result = []
        current = ''
        N = len(s)
        if N > 12 or N < 4:
            return []
        __dfs(s,result,current,0,N,0)
        return result

        
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
    # inputList = [2, 2]
    # time = 3
    # beginWord = "ymain"
    # endWord = "oecij"
    # wordList = ["ymann","yycrj","oecij","ymcnj","yzcrj","yycij","xecij","yecij","ymanj","yzcnj","ymain"]
    s1 = "great"
    s2 = "rgeat"
    s1 = "abcde"
    s2 = "caebd"
    nums = [1,2,2]
    nums = [4,4,4,1,4]
    # nums = [0]
    s = "25525511135"
    s = "010010"
    s = "1111"
    s = "101023"
    result = solu.restoreIpAddresses(s)

    output_Str = ' result = ' + str(result)
    print(output_Str)
    
