# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 10:46:33 2021

@author: qizhe
"""

class Solution:
    def countMaxOrSubsets(self, nums) -> int:
        """
        感觉按位或的最大值就是所有元素或起来的最大值呢
        集合自身一定满足这个条件
        暴力搜索试试
        """
        aim = 0
        for i in nums:
            aim |=i
            
        def dfs(nums,result,current,currentResult,aim,used,begin,length):
            
            if begin == length:
                return
            if currentResult == aim:
                # print(current)
                result[0] +=1
                # return
            
            for i in range(begin,length):
                # print(begin,length)
                if used[i]:
                    continue
                used[i] = True
                dfs(nums,result,current+[nums[i]],currentResult|nums[i],aim,used,i,length)
                used[i] = False
                # break
            
            
            
            return
        N = len(nums)
        result = [0]
        current = []
        used = [False] * N 
        dfs(nums,result,current,0,aim,used,0,N)
        return result[0]
        


if __name__ == '__main__':
    solu = Solution()
    
    input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    input_List = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    # input_List = 1
    nums = [3,1]
    # nums = [2,2,2]
    nums = [3,2,1,5]
    result = solu.countMaxOrSubsets(nums)

    output_Str = ' result = ' + str(result)
    print(output_Str)