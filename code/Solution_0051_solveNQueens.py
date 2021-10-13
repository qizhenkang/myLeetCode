# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 17:15:32 2021

@author: qizhe
"""

class Solution:
    def solveNQueens(self, n: int):
        """
        典型的回溯问题
        读题目，他要的是，所有解，不是找到一个就可以
        
        感觉不难呢为什么？
        # 搞一个队列/栈，保存当前剩余的行/列，
        感觉搞一个同等大小的bool矩阵，保存可选位置
        感觉又有点像动态规划，可以逐级扫描来解决，保存斜率信息，帮助决策。
        
        核心思路是，从左上到右下逐个扫描，判断是否可行，若可行则填入；
        是否可行的思路，是利用状态来定义，状态表由位运算来确定：
        0000 0000 
        第 0 位 - 是否该位置存在 queen
        第 1 位 - 左上存在 queen
        第 2 位 - 竖向存在 queen
        第 3 位 - 右上存在
        第 4 位 - 左侧存在
        
        这个方法有点问题，好像是找不全，思路错了应该
        """
        
        # def dfs(n,result,current,row,valid):
            
        #     if num == n:
        #         result.append(current)
        #         return
            
        #     for i in range(row,n*n):
        #         # print(i,result)
        #         if validPosition[i//n][i % n]:
                    
        #             for k in range(n*n):
        #                 if k == i//n or k == i%n or (abs(i - k) % (n-1)) == 0 or (abs(i - k) % (n+1)) == 0:
        #                     validPosition[k//n][k % n] = False
        #     dfs(n,result,current+[i],num+1,validPosition)
        #             break
        #     return
        if n == 1:
            return [['Q']]
        elif n == 2 or n == 3:
            return []
        
        result = []
        current = []
         
        # dfs(n,result,current,0,validPositionStack)
        queenCnt = 0
        # endFlag = 1
        notFlag = 0
        notvalidNUM = 0b11111
        for x in range(0,n):
            valid = [[0]*n for _ in range(n)]
            valid[0] = [0]*n
            valid[0][x] = notvalidNUM
            current = []
            current.append([0,x])
            queenCnt = 1
            for i in range(1,n):
                for j in range(n):
                    notFlag = 0
                    
                    notvalid1 = valid[i-1][j-1] >> 1 & 0b1 if j>0 else 0
                    notvalid2 = valid[i-1][j] >> 2 & 0b1
                    notvalid3 = valid[i-1][j+1] >> 3 & 0b1 if j<n-1 else 0
                    notvalid4 = valid[i][j-1] >> 4 & 0b1 if j>0 else 0
                    # 上面相量是否存在
                    if i != 0 and (notvalid1 or notvalid2 or notvalid3 or notvalid4):
                        # 上面存在 则本位也记一下
                        valid[i][j] |= notvalid1 << 1
                        valid[i][j] |= notvalid2 << 2
                        valid[i][j] |= notvalid3 << 3
                        valid[i][j] |= notvalid4 << 4
                        notFlag = 1
                    
                    # 若合法，则加入
                    print(x,i,j,not notFlag, bin(valid[i][j]),queenCnt)
                    if not notFlag:
                        valid[i][j] = notvalidNUM
                        current.append([i,j])
                        queenCnt +=1
                    
                    if queenCnt >= n:
                        # result
                        resultStr = ['']*n 
                        for i in range(n):
                            temp = ['.'] * n
                            temp[current[i][1]] = 'Q'
                            resultStr[i] = ''.join(temp)
                        result.append(resultStr)
                        break
                        # return result


        
        return result

if __name__ == '__main__':
    solu = Solution()
    
    input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    input_List = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    # input_List = 1

    result = solu.solveNQueens(5)

    output_Str = ' result = ' + str(result)
    print(output_Str)
