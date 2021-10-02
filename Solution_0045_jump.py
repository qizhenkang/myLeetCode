# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 10:41:49 2021

@author: qizhe
"""

class Solution:
    def jump(self, nums) -> int:
        """
        第一反应有点像动态规划，又有点像回溯
        回溯：第一次提交竟然超时了，是不是不应该暴力深度搜索？
        4616 ms	15.4 MB
        
        动态规划：找状态转移，第一次成功了，但用时还是太长，可以进一步优化
        36 ms	15.3 MB
        与答案思路一致
        """
        N = len(nums)
        currPosi = 0
        cnt = 0
        while currPosi < N - 1:
            optimalVal = 0
            for j in range(currPosi+1,min(currPosi+nums[currPosi]+1,N)):
                if j == N-1:
                    currPosi = N-1
                    break
                if optimalVal <= nums[j] + j:
                    optimalVal = nums[j] + j
                    currPosi = j
            print(currPosi)
            cnt += 1
        return cnt
        # def dfs(result,current,begin,length,nums):
        #     print(current,begin,length-1,result)
        #     if begin == length-1:
        #         return len(current)-1
        #     for i in range(begin+1,min(begin + nums[begin] + 1,length)):
        #         if result < len(current):
        #             break
        #         result = min(result,dfs(result,current + [nums[i]],i,length,nums))
        #     return result
        # N = len(nums)
        # current = [nums[0]]

        # return dfs(N,current,0,N,nums)
        
        
        
if __name__ == '__main__':
    solu = Solution()
    
    input_List = [2,3,1]
    
    # input_List = 1

    result = solu.jump(input_List)

    output_Str = ' result = ' + str(result)
    print(output_Str)