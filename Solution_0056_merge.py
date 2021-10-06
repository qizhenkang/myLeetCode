# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 19:30:22 2021

@author: qizhe
"""

class Solution:
    def merge(self, intervals):
        """
        读题：
        1、没懂要考什么，我知道他要做的是把所有区间进行合并
        2、能不能，读所有的区间，记录所有的，然后将这个区间重新划分？
        3、能不能，排序，按起始点从小到大排
        
        测试：
        1、通过，用时94% 内存23%
        
        答案：
        与答案思路一致
        
        """
        result = []
        # tuple(intervals)
        intervals.sort(key = lambda x:x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        for i in intervals:
            if end < i[0]:
                result.append([start,end])
                start = i[0]
                end = i[1]
                continue

            if end < i[1]:
                end = i[1]
            
        result.append([start,end])

        return result
        
        
        
        
        
        
        
if __name__ == '__main__':
    solu = Solution()
    
    # input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    # input_List = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    intervals = [[0,0],[1,1]]
    # input_List = [[1,2,3],[4,5,6],[7,8,9]]
    # input_List = 1
    # numerator = -50
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    result = solu.merge(intervals)

    output_Str = ' result = ' + str(result) 
    print(output_Str)