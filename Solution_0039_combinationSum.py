# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 16:16:13 2021

@author: qizhe
"""

class Solution:
    def combinationSum(self, candidates, target: int):
        """
        看了答案的思想，感觉有些收获，本质上就是一个经典的“回溯”算法
        """
        
        def dfs(candidates,begin,length,path,result,target):
            
            # if target <0:
            #     return
            if target == 0:
                result.append(path)
                return
            
            for i in range(begin,length):
                # 排序之后，可以剪枝
                targetNext = target - candidates[i]
                if targetNext < 0:
                    break
                # print('0',path)
                dfs(candidates, i, length, path + [candidates[i]], result, targetNext)
                # print('        1',path)
            
            return
        
        N = len(candidates)
        if N == 0:
            return []
        
        candidates.sort()
        result = []
        path = []
        
        dfs(candidates,0,N,path,result,target)
        
        return result
        

        
if __name__ == '__main__':
    solu = Solution()
    input_List = [2,3,6,7]
    # input_List = [4,3,2,1]
    # input_List = [4,5,6,7,0,1,2]
    input_aim = 7
    result = solu.combinationSum(input_List,input_aim)

    # while result:
    #     print(result.val)
    #     result = result.next
    output_Str = 'result = ' + str(result)
    print(output_Str)