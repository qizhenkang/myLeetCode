# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 09:43:47 2021

@author: qizhe
"""

class Solution:
    def numberOfBoomerangs(self, points) -> int:

        result = 0
        
        for pi in points:
            distdict = {}
            for pj in points:
                dist = (pi[0] - pj[0])**2 + (pi[1] - pj[1])**2
                if dist not in distdict:
                    distdict[dist] = 1
                else:
                    distdict[dist] += 1 
            for m in distdict.values():
                # print(distdict)
                result += m*(m-1)
        return result

        


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    input_List =[[0,0],[1,0],[2,0]]
    # input_List = TreeNode(1)
    # input_List.left = TreeNode(2)
    # input_List.right = TreeNode(3)
    
    result = solu.numberOfBoomerangs(input_List)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)