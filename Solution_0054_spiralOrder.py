# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 16:11:15 2021

@author: qizhe
"""

class Solution:
    def spiralOrder(self, matrix):
        """
        读题：
        1、这题一看就有思路啊，就是一个循环加换向的感觉，能不能有更简单的思路
        2、螺旋之后，边界变了，不是很简单，要想办法处理边界
        思路：
        1、如果不顾空间，就开一个一模一样的数组，用来存储True or False
        2、如果顾空间，需要保存每行/每列的边界
        
        测试：
        1、用了顾空间的方案，用时击败86%，内存消耗击败5%，看来有问题
        2、看答案后修改，用时击败86%，内存消耗击败84%，成功
        
        
        答案：
        1、方法一：遍历，然后建立一个同等大小的矩阵，True and False
        2、方法二：按层遍历
        
        我的方案：
        1、依然是模拟的方案
        2、但是不要那么多空间了，我们只保存每行/每列的边界就好了
        3、最终优化，我们只保存横向边界和纵向边界就好了
        
        """
        result = []
        rowMax = len(matrix)
        colMax = len(matrix[0])
        # rowBound = [[-1,colMax] for _ in range(rowMax)]
        # colBound = [[-1,rowMax] for _ in range(colMax)]
        rowBound = [-1,colMax]
        colBound = [-1,rowMax] 
        direction = [0,1]
        cnt = 0
        i = 0
        j = 0
        # rowBound[0] = [0,colMax]
        # colBound[0] = [0,rowMax]
        while cnt < rowMax * colMax:
            # 向前一步走，判断是否越界
            print(i,j,direction,rowBound,colBound)
            result.append(matrix[i][j])
            
            # 移动
            directionCnt = 4
            moveFlag = 0
            while directionCnt>0 and not moveFlag:
                # print(directionCnt,moveFlag,direction)
                if direction[1]:
                    if j + direction[1] < rowBound[1] and j + direction[1] > rowBound[0]:
                        j += direction[1]
                        moveFlag = 1
                    else:
                        direction = [direction[1],0] 
                else:
                    if i + direction[0] < colBound[1] and i + direction[0] > colBound[0]:
                        i += direction[0]
                        moveFlag = 1
                    else:
                        direction = [0,-direction[0]]
                directionCnt -= 1
            
            # 更新边界
            if direction[1]:
                if direction[1] > 0:
                    colBound[0] = max(colBound[0],i)
                else:
                    colBound[1] = min(colBound[1],i)
            else:
                if direction[0] > 0:
                    rowBound[1] = min(rowBound[1],j)
                else:
                    rowBound[0] = max(rowBound[0],j)
            
            # print(i,j,direction,rowBound,colBound)
            
            cnt +=1
                    
        
        return result
        

if __name__ == '__main__':
    solu = Solution()
    
    input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    input_List = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    input_List = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    # input_List = [[1,2,3],[4,5,6],[7,8,9]]
    # input_List = 1
    # numerator = -50
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    result = solu.spiralOrder(input_List)

    output_Str = ' result = ' + str(result) 
    print(output_Str)