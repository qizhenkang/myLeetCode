# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 14:57:44 2021

@author: qizhe
"""
from typing import List
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        """
        读题：
        1、不知道有没有好办法，但总得来说就是模拟
        2、从输入数据来看，时间复杂度需要是On的
        
        测试：
        1、确实心里没底，第一次测试，通过了28/29
        2、看了一下案例，是右下方有一种情况没有考虑到
        3、终于通过了，性能不好
        
        答案：
        1、看了一下答案，也没啥意思，找规律
        """
        x = 0
        y = 0
        boundMax = 1e6
        x0,y0 = x,y
        direction = [[0,1],[-1,0],[0,-1],[1,0]]
        track = [[0,0],[0,0],[0,0],[0,0]]
        rightBound = x
        upBound = boundMax # 第一步的y坐标
        leftBound = -boundMax # 第2步的x坐标
        downBound = -boundMax # 第3步的y坐标
        stepNum = 0
        state = 0 # 两种状态
        teState = 0
        boundSquare = [0,0,0,0]
        # if len(distance) % 4:
        #     for i in range(4 - len(distance) % 4):
        #         distance.append(0)
        # print(distance)
        for i in range(len(distance)):
            stepNum = i % 4
            x += direction[stepNum][0] * distance[i]
            y += direction[stepNum][1] * distance[i]
            track[stepNum] = [x,y]
            if not teState and (stepNum == 0 and y >= upBound or stepNum == 1 and x <= leftBound or stepNum == 2 and y <= downBound or stepNum == 3 and x >= rightBound and y >= y0):
                # print('state0', stepNum,x,y)
                return True
            if state and boundSquare[0] <= x <= boundSquare[2] and boundSquare[1] <= y <= boundSquare[3]:
                print('stRate1',teState, stepNum,x,y,boundSquare,upBound,leftBound,downBound)
                if not teState or (y >= upBound or stepNum == 1 and x <= leftBound or stepNum == 2 and y <= downBound or stepNum == 3 and x >= rightBound and y >= y0):
                    return True
            # 更新坐标
            if stepNum == 3:
                if not state:
                    if track[3][0] - x0 < 0:
                        # 第2/3象限处理
                        rightBound = track[3][0]
                        upBound = track[0][1] # 第一步的y坐标
                        leftBound = track[1][0] # 第2步的x坐标
                        downBound = track[2][1] # 第3步的y坐标
                        state = 0
                    else:
                        # 第4象限处理（第1象限前面必然已经处理了）
                        state = 1
                        teState = 1
                        # 记录现有的边界，其实是一个小矩形
                        rightBound = track[3][0]
                        upBound = y0
                        leftBound = track[2][0]
                        downBound = track[2][1]
                        boundSquare = [track[2][0],track[2][1],track[0][0],track[0][1]]
                else:
                    # 原本就是state
                    boundSquare[2] = track[0][0]
                    boundSquare[3] = track[0][1]
                    teState = 0
                    # print(track,boundSquare)
                    if track[3][1] - y0 >= 0 or track[3][0] - boundSquare[0] < 0:
                        rightBound = track[3][0]
                        upBound = track[0][1] # 第一步的y坐标
                        leftBound = track[1][0] # 第2步的x坐标
                        downBound = track[2][1] # 第3步的y坐标
                        state = 0
                    elif track[3][1] - y0 < 0 and track[3][0] - boundSquare[2] <= 0:
                        # 在原来的正下方
                        # print('zxf')
                        rightBound = track[3][0]
                        upBound = y0 # 第一步的y坐标
                        leftBound = track[1][0] # 第2步的x坐标
                        downBound = track[2][1] # 第3步的y坐标
                        # print(rightBound,upBound,leftBound,downBound)
                        state = 0
                    else:
                        # 在右下方
                        # print('yxf')
                        teState = 1
                        rightBound = track[3][0]
                        upBound = boundSquare[1]
                        leftBound = boundSquare[0]
                        downBound = track[2][1]
                        boundSquare = [track[2][0],track[2][1],track[0][0],track[0][1]]
                
                x0,y0 = track[3][0],track[3][1]
        # print(x,y,boundSquare)
        return False
    


if __name__ == '__main__':
    solu = Solution()
    distance = [2,1,1,2]
    distance = [1,2,3,4]
    d = [[2,1,1,2],[1,2,3,4],[1,1,1,1],[1,2,3,4,5,5,8,6],[1,1,3,2,1,1],[1,1,2,2,3,1,1]]
    for distance in d:
        result = solu.isSelfCrossing(distance)
    
        # output_Str = 'result = ' + solu.intToRoman(input_int)
        output_Str = ' result = ' + str(result)
        print(output_Str)