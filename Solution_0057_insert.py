# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:14:42 2021

@author: qizhe
"""

class Solution:
    def insert(self, intervals, newInterval):
        
        """
        10分钟没写出来，待定，感觉有点麻烦，是不是有更好的思路？
        
        这题做的很差，没有找到思路，通过了 用时超过99.5% 内存超过5% 看来有问题，应该有套路，是不是动态规划啥的？
        """
        
        N = len(intervals)
        if N == 0:
            return [newInterval]
        poplist = []
        state = 0
        endFlag = 0
        for i in range(N):
            # 在现有区域之内
            if not state and intervals[i][0] <= newInterval[0] <= intervals[i][1]:
                # 包含在内，直接结束
                if newInterval[1] <= intervals[i][1]:
                    break
                state = 1
                
            # 在现有区域之外
            if not state and newInterval[0] < intervals[i][0]:
                if newInterval[1] >= intervals[i][0]:
                    intervals[i][0] = newInterval[0]
                else:
                    intervals.insert(i,newInterval)
                    # endFlag = 1
                    break
                if newInterval[1] <= intervals[i][1]:
                    break
                state = 1
            
            if not state and newInterval[0] > intervals[i][0] and i == N-1:
                intervals.append(newInterval)
                endFlag = 1
                
            if state:
                intervals[i][1] = max(intervals[i][1],newInterval[1])
                for j in range(i+1,N):
                    # 判断后续，共三种情况：
                    # 1 够不到后一个，直接结束即可，最简单
                    if newInterval[1] < intervals[j][0]:
                        intervals[i][1] = newInterval[1]
                        endFlag = 1
                        break
                    # 2 在后一个范围内，也可以结束，简单
                    elif newInterval[1] <= intervals[j][1]:
                        # 两个合并
                        intervals[i][1] = intervals[j][1]
                        # intervals.pop(j)
                        poplist.append(j)
                        endFlag = 1
                        break
                    # 3 超过了后一个的范围，应删除，简单
                    else:
                        poplist.append(j)
                        
                    if j == N-1:
                        intervals[i][1] = newInterval[1]
                        endFlag = 1
            if endFlag:
                break
        
        for popnumber in poplist[::-1]:
            # print(poplist,popnumber)
            intervals.pop(popnumber)
                
        return intervals

        

if __name__ == '__main__':
    solu = Solution()
    
    # input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    # input_List = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    intervals = "Hello, my name is John"
    intervals = [[1,1],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [2,17]
    intervals = [[2,5]]
    newInterval = [5,7]
    # input_List = 1
    # numerator = -50
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    result = solu.insert(intervals, newInterval)

    output_Str = ' result = ' + str(result) 
    print(output_Str)