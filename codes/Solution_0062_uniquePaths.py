# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 18:35:47 2021

@author: qizhe
"""
import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        读题：
        1、一看是一个暴力搜索，第一反应是回溯，又有点感觉像动态规划
        2、没看出有别的好办法
        3、回溯思路：向右或向下走，这里会有一些可以简化的地方
        4、简化：1 m n 可以互换， 
        
        测试：
        1、回溯超时了，看来需要剪枝，或者有点像动态规划
        2、想了一下，好像是一个排列组合的问题
        
        答案：
        排列组合 + 动态规划 我吐了……
        """
        # return comb(m + n - 2, n - 1)

        # if m > n:
        #     m, n=n, m
        
        # result = 1
        
        # for x in range(n,m + n - 1):
        #     result *=x
        
        # for x in range(1,m):
        #     result /=x
        
        # return round(result)

        return round(math.factorial(m + n - 2) / math.factorial(n-1) / math.factorial(m-1))
        
        # def dfs(i,j,m,n):
        #     if i == m-1 and j == n-1:
        #         return 1
        #     if i >= m or j >=n:
        #         return 0
            
        #     return dfs(i+1, j, m, n) + dfs(i, j+1, m, n)
        
        # return dfs(0,0,m,n)

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
    m = 3
    n = 1
    result = solu.uniquePaths(m,n)
    # output_Str = ' result = '
    # print(' result = ',end=' ')
    # while result:
    #     print(result.val,end=' ')
    #     result = result.next


    output_Str = ' result = ' + str(result) 
    print(output_Str)