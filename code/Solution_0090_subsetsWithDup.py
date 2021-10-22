# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 11:06:36 2021

@author: qizhe
"""
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        读题：
        1、nums里面可能有重复元素，这会给我们造成一定困难
        2、基本的思想是回溯
        
        测试：
        1、5分钟就写完了回溯，测试了一下 过了15/20 错误了
        2、理解题意有点问题，应该返回子集，也就是不考虑顺序的
        3、第二次通过了，7分钟解决
        4、简单优化了一下，内存消耗击败82%
        
        答案：
        1、回溯一样
        2、能不能用栈来实现DFS，毕竟工程中递归少一些
        3、递归的本质，是利用了栈
        
        """
        
        # --------------------     Stack DFS -----------------------
        result = [[]]
        current = []
        stack = [0]
        curStack = [[]]
        N = len(nums)
        nums.sort()
        while stack:
            for x in range(len(stack)):
                current = curStack.pop()
                for i in range(stack.pop(), N):
                    if current + [nums[i]] not in result:
                        stack.append(i+1)
                        curStack.append(current + [nums[i]])
                        result.append(current + [nums[i]])
        return result
    
        # -------------------- Recursion DFS     -----------------------
        # def __dfs(nums,result,current,begin,length):
        #     print(current)
        #     result.append(current)
        #     for i in range(begin,length):
        #         if current + [nums[i]] not in result:
        #             __dfs(nums,result,current + [nums[i]],i+1,length)
        # current = []
        # result = []
        # N = len(nums)
        # nums.sort()
        # __dfs(nums,result,current,0,N)
        # return result
        
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
    result = solu.subsetsWithDup(nums)

    output_Str = ' result = ' + str(result)
    print(output_Str)