# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 22:36:33 2021

@author: qizhe
"""

class Solution:
    def permuteUnique(self, nums):
        """
        求全排列，存在重复数字，排序+深度优先遍历 就可以解了
        这个自己没做出来，看了答案，关键点在于存在重复时的处理
        和之前的不同点还有就是，这个顺序是认为重要的
        
        突然想到，回溯算法是一种深度优先算法，存在剪枝。
        这与人工神经网络训练/蒙特卡洛那些非常一致，都是在解一个NP问题，
        方法是，通过深度优先搜索+合理剪枝，快速地得到局部最优解
        而不关心全局最优
        """
        
        def dfs(nums,result,current,begin,length,used):
            # print(current)
            if len(current) == length:
                result.append(current)
                return
            
            for i in range(begin,length):
                if used[i]:
                    continue
                # usednow = used.remove
                if i > begin and nums[i] == nums[i-1] and used[i-1]:
                    continue
                used[i] = True
                # print(used)
                dfs(nums, result, current + [nums[i]], begin, length, used)
                used[i] = False
            
            
            return
        N = len(nums)
        if not N:
            return []
        result = []
        current = []
        used = [False] * N 
        nums.sort()
        dfs(nums,result,current,0,N,used)
        return result
    
if __name__ == '__main__':
    solu = Solution()
    # input_List =  [2]
    input_List = [2,1,1]
    # input_List = [4,5,6,7,0,1,2]
    # input_aim = 0
    result = solu.permuteUnique(input_List)

    # while result:
    #     print(result.val)
    #     result = result.next
    output_Str = 'result = ' + str(result)
    print(output_Str)