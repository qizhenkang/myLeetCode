# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 10:21:32 2021

@author: qizhe
"""

class Solution:
    def minimumTotal(self, triangle) -> int:
        """
        
        第一反应：
        这题让找三角形的最小路径，感觉有点难，像是一个深度优先搜索
        这是不是所谓的，满二叉树的深度优先搜索啊
        可以所谓的“剪枝”？记录最短路径，从而超过时就剪枝
        
        答案思路：
        是一道20年前的国际竞赛题，不应用遍历的方法，是典型的动态规划问题
        
        我的思路：
        从下往上走，可以减少最后的一个取最值

        Parameters
        ----------
        triangle : TYPE
            DESCRIPTION.

        Returns
        -------
        int
            DESCRIPTION.

        """
        # 按动态规划来做的话，需要构造问题，也就是第i层的最短路径
        # result = 1e6
        
        N = len(triangle)
        
        dp = triangle[-1]
        
        for j in range(N-1,0,-1):
            for i in range(j):
                # 从下往上走，留到最后的就是最小值
                # 这样只需要遍历一次
                dp[i] = min(dp[i],dp[i+1]) + triangle[j-1][i]
                # print(j,i,dp)
        return dp[0]
        
        
        
        
        
        
if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_list =
    input_List = [[2],[3,4],[6,5,7],[4,1,8,3]]
    # input_List = [[-10]]
    # input_int = 6

    result = solu.minimumTotal(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)