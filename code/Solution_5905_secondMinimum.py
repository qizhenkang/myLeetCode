# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 11:00:46 2021

@author: qizhe
"""
from sortedcontainers import SortedList

class Solution:
    def secondMinimum(self, n: int, edges, time: int, change: int):
        """
        所谓的备选路线
        划分：
        1、首先，要确定一共有几条路
        2、其次，计算路线时间
        3、想办法找到最快路线
        """
        # 这里应该是回溯找路
        def dfs(lines,edges,current,n,begin):
            # print(begin)
            if current[-1] == n or begin >= len(edges):
                lines.append(current)
                return
            nowNode = current[-1]
            for i in range(len(edges)):
                # print(begin,i,current,len(edges),len(lines),lines)
                if len(lines) > 20:
                    return
                if edges[i][0] == nowNode and edges[i][1] not in current:
                    dfs(lines,edges,current+[edges[i][1]],n,i)
                elif edges[i][1] == nowNode and edges[i][0] not in current:
                    dfs(lines,edges,current+[edges[i][0]],n,i)
            return
        
        # nowNode = 1
        current = [1]
        lines = []
        dfs(lines,edges,current,n,0)
        
        
        
        if len(lines) == 1:
            # 只有一条路的时候
            lines.append(lines[0] + [lines[0][-2],n])
        lines.append([1,2,4,1,2,5,6])
        print(lines)
        linesTime = SortedList() # 有序列表
        for i in range(len(lines)):
            nowTime = -time
            for j in range(len(lines[i])):
                nowTime += time
                if j < len(lines[i])-1 and (nowTime // change) % 2:
                    nowTime = (nowTime // change + 1)*change
                    # print(nowTime,change)
            # linesTime.append(nowTime)
            linesTime.add(nowTime)
        print(linesTime)
        
        return linesTime[1]

if __name__ == '__main__':
    solu = Solution()

    nums = [3,2,1,5]
    n = 5
    edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
    time = 3
    change = 5
    
    n = 2
    edges = [[1,2]]
    time = 3
    change = 2
    
    # n = 12
    # edges = [[1,2],[1,3],[3,4],[2,5],[4,6],[2,7],[1,8],[5,9],[3,10],[8,11],[6,12]]
    # time = 60
    # change = 600
    
    # n = 11
    # edges = [[1,2],[1,3],[1,4],[2,5],[5,6],[3,7],[4,8],[4,9],[9,10],[10,11]]
    # time = 8
    # change = 584
    n = 6
    edges = [[1,2],[2,3],[2,4],[2,5],[5,6],[4,1],[5,3]]
    time = 457
    change = 953
    n = 19
    edges = [[1,2],[2,3],[1,4],[2,5],[2,6],[2,7],[7,8],[8,9],[7,10],[9,11],[11,12],[1,13],[3,14],[13,15],[14,16],[8,17],[4,18],[11,19],[17,11],[3,19],[19,7],[12,5],[8,1],[15,7],[19,6],[18,9],[6,8],[14,19],[13,18],[15,2],[13,12],[1,5],[16,18],[3,16],[6,1],[18,14],[12,1],[16,6],[13,11],[1,14],[16,13],[11,16],[4,15],[17,5],[5,9],[12,2],[4,10],[9,16],[17,9],[3,5],[10,2],[18,1],[15,18],[12,17],[10,6],[10,18],[19,12],[12,15],[19,13],[1,19],[9,14],[4,3],[17,13],[9,3],[17,10],[19,10],[5,4],[5,7],[14,17],[1,10],[4,11],[6,4],[5,10],[7,14],[8,14],[18,17],[15,10],[11,8],[14,11],[7,3],[5,18],[13,8],[4,12],[11,3],[5,15],[15,9],[8,10],[13,3],[17,1],[10,11],[15,11],[19,2],[1,3],[7,4],[18,11],[2,14],[9,1],[17,15],[7,13],[12,16],[12,8],[6,12],[9,6],[2,17],[15,6],[16,2],[12,7],[7,9],[8,4]]
    time = 850
    change = 411
    result = solu.secondMinimum(n, edges, time, change)

    output_Str = ' result = ' + str(result)
    print(output_Str)