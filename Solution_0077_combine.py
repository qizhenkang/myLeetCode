# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 10:09:55 2021

@author: qizhe
"""

class Solution:
    def combine(self, n: int, k: int):
        """
        1-n组成k个数的组合
        10min结束
        """
        def dfs(result,current,begin,n,k):
            if len(current) == k:
                result.append(current)
                return
            
            for i in range(begin,n+1):
                
                dfs(result,current + [i],i + 1,n,k)

            return
        result = []
        current = []
        dfs(result,current,1,n,k)
        return result

        





if __name__ == '__main__':
    solu = Solution()
    # input_List = [4,5,6,7,0,1,2]
    # input_aim = 0
    result = solu.combine(4,2)

    # while result:
    #     print(result.val)
    #     result = result.next
    output_Str = 'result = ' + str(result)
    print(output_Str)