# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 00:06:44 2021

@author: qizhe
"""

class Solution:
    def destCity(self, paths):
        """
        基本思路：哈希表记录次数，若仅1次的，则为
        """
        pathDict = {}
        for path in paths:
            if path[0] in pathDict:
                pathDict[path[0]] += 1
            else:
                pathDict[path[0]] = 1
        
            if path[1] not in pathDict:
                pathDict[path[1]] = 0
        
        for key,value in pathDict.items():
            if value == 0:
                return key
        
        return
            
        
        
if __name__ == '__main__':
    solu = Solution()
    # input_List =  [2]
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    # paths = [["B","C"],["D","B"],["C","A"]]
    # paths = [["A","Z"]]
    # input_List = [4,5,6,7,0,1,2]
    # input_aim = 0
    result = solu.destCity(paths)

    # while result:
    #     print(result.val)
    #     result = result.next
    output_Str = 'result = ' + str(result)
    print(output_Str)