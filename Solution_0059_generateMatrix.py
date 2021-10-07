# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 10:51:43 2021

@author: qizhe
"""
"""
1、所有公式编号 48字体49
2、14页 - 页边距

研究实施方案 一页纸 每一点都要有图
"""
class Solution:
    def generateMatrix(self, n: int):
        """
        这题 和 54 spiralOrder 思路一致， 复制了一下 只改了几个地方
        用时击败96%，内存消耗击败62%，成功
        """
        result = [[0]*n for _ in range(n)]
        # rowBound = [[-1,colMax] for _ in range(rowMax)]
        # colBound = [[-1,rowMax] for _ in range(colMax)]
        rowBound = [-1,n]
        colBound = [-1,n] 
        direction = [0,1]
        cnt = 1
        i = 0
        j = 0
        # rowBound[0] = [0,colMax]
        # colBound[0] = [0,rowMax]
        while cnt <= n * n:
            # 向前一步走，判断是否越界
            print(i,j,direction,rowBound,colBound)
            result[i][j] = cnt
            
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
    
    # input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    # input_List = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    # intervals = "Hello, my name is John"
    # input_List = [[1,2,3],[4,5,6],[7,8,9]]
    input_List = 4
    # numerator = -50
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    result = solu.generateMatrix(input_List)

    output_Str = ' result = ' + str(result) 
    print(output_Str)