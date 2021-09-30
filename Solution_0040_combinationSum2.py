# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 17:48:40 2021

@author: qizhe
"""

class Solution:
    def combinationSum2(self, candidates, target: int):
        """
        回溯算法的再次使用，成功了
        17:48 - 18:07
        20min解决
        """
        def dfs(candidates, target, current, begin, length):
            if target == 0:
                if current:
                    result.append(current)
                return
            for i in range(begin,length):
                targetNew = target - candidates[i]
                if targetNew < 0:
                    break

                # print('0',current,candidates[i], candidates[i-1])
                if i > begin and candidates[i] == candidates[i-1]:
                    continue
                dfs(candidates, targetNew, current + [candidates[i]], i+1, length)
                # print('               1',current)

            return
        N = len(candidates)
        result = []
        current = []
        candidates.sort()
        dfs(candidates, target, current, 0, N)
        
        return result
        
        


        
if __name__ == '__main__':
    solu = Solution()
    input_List =  [2]
    # input_List = [4,3,2,1]
    # input_List = [4,5,6,7,0,1,2]
    input_aim = 0
    result = solu.combinationSum2(input_List,input_aim)

    # while result:
    #     print(result.val)
    #     result = result.next
    output_Str = 'result = ' + str(result)
    print(output_Str)