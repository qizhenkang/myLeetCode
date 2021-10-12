# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 16:54:01 2021

@author: qizhe
"""

class Solution:
    def groupAnagrams(self, strs):
        """
        读题：因为要判断是否为相同字母构成，因此想构建哈希表
        不会做
        看答案后：
        这道题的本质，是要提取_字符串的特征_
        答案给了两种思路：
        1、对字符串排序，相同字母构成，排序之后必然一致
        2、哈希表，判断字母构成
        本文采用了第二种思路，本质上是两层哈希表的嵌套
        """

        strsDict = {}
        
        for st in strs:
            cnt = [0] * 26
            
            for s in st:
                cnt[ord(s) - ord('a')] += 1
            # print(tuple(cnt))
            tuple_cnt = tuple(cnt)
            if tuple_cnt in strsDict:
                strsDict[tuple_cnt].append(st) 
            else:
                strsDict[tuple_cnt] = []
                strsDict[tuple_cnt].append(st) 
        
        return list(strsDict.values())
        
        


if __name__ == '__main__':
    solu = Solution()
    
    input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    input_List = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    # input_List = 1
    numerator = -50
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    result = solu.groupAnagrams(strs)

    output_Str = ' result = ' + str(result) 
    print(output_Str)