# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 11:00:46 2021

@author: qizhe
"""
from sortedcontainers import SortedList
from collections import defaultdict, deque
from typing import List

class Solution:
    def secondMinimum(self, n: int, edges, time: int, change: int):
        """
        所谓的备选路线
        划分：
        1、首先，要确定一共有几条路
        2、其次，计算路线时间
        3、想办法找到最快路线
        
        用了BFS之后，还是存在问题，应该是在BFS里直接结束就是了，不应该再DFS了的，明天再改改试试
        
        测试：
        1、改进后，只用BFS，超时了
        2、第二次改进，建立了一个Dict，成功了
        
        这题可能错了10次了吧，就成功这一次，就一个典型的BFS
        """
        # 这里应该是BFS，建立图
        def __bfs(edgesDict,n,time,change):
            
            queue = deque()
            queue.append(1)
            Visited = set()
            nextVisited = set()
            currentVisited = set()
            Visited.add(1)
            
            found = 0
            depth = 0
            currentTime = 0
            newTime = 0
            result = []
            while queue:
                depth += 1
                newTime = time + ((currentTime) // change + 1) * change if (currentTime // change) % 2 else  currentTime + time
                currentTime = newTime
                # 建立图
                queueLength = len(queue)
                # print(queue)
                for i in range(queueLength):
                    
                    nodeNow = queue.popleft()
                    currentVisited.add(nodeNow)
                    nodeNew = 0
                    # 找下一个
                    for nodeNew in edgesDict[nodeNow]:
                        # 只要没访问过
                        if nodeNew not in Visited:
                            if nodeNew == n:
                                if result:
                                    if result[0] != currentTime:
                                        result.append(currentTime)
                                        found += 1
                                else:
                                    result.append(currentTime)
                                    found += 1
                                # print(currentTime,result,found)
                                if found >= 2:
                                    break
                                
                            if nodeNew not in nextVisited:
                                nextVisited.add(nodeNew)
                                queue.append(nodeNew)
                            # lines[nodeNow].add(nodeNew)
                    if found >= 2:
                        break
                Visited |= currentVisited
                currentVisited = set()
                nextVisited = set()
                if found >= 2:
                    break

            return result

        
        # nowNode = 1
        
        # 构造字典表，用于找路
        edgesDict = defaultdict(set)
        for edge in edges:
            edgesDict[edge[0]].add(edge[1])
            edgesDict[edge[1]].add(edge[0])

        # print(edgesDict)

        result = __bfs(edgesDict,n,time,change)
        
        # 如果只有一条路
        if len(result) == 1:
            currentTime = result[0]
            currentTime = time + ((currentTime) // change + 1) * change if (currentTime // change) % 2 else  currentTime + time
            newTime = time + ((currentTime) // change + 1) * change if (currentTime // change) % 2 else  currentTime + time
            result.append(newTime)
        minTime = result[0]
        for re in result:
            if minTime != re:
                minTime = re
        # second
        return minTime
        
        
        


if __name__ == '__main__':
    solu = Solution()

    # nums = [3,2,1,5]
    n = 5
    edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
    time = 3
    change = 5
    
    # n = 6
    # edges = [[1,2],[1,3],[2,4],[3,5],[5,4],[4,6]]
    # time = 3
    # change = 100
    
    n = 2
    edges = [[1,2]]
    time = 3
    change = 2
   
    # n = 2
    # edges = [[1,2]]
    # time = 1
    # change = 2
    # n = 12
    # edges = [[1,2],[1,3],[3,4],[2,5],[4,6],[2,7],[1,8],[5,9],[3,10],[8,11],[6,12]]
    # time = 60
    # change = 600
    
    n = 11
    edges = [[1,2],[1,3],[1,4],[2,5],[5,6],[3,7],[4,8],[4,9],[9,10],[10,11]]
    time = 8
    change = 584
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