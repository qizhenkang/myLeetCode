# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 23:15:50 2021

@author: qizhe
"""

class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        初步的想法是：
        1、深度优先搜索，及时剪枝，也就是所谓的回溯法
        2、每个点受到横+竖+3x3方格的限制，可以得到可选的数字
        3、来吧
        
        花了50分钟通过了，没有看答案
        有时间再优化一下的
        """
        def dfs(board,i,j, length):
            # print('Start: ',i,j)
            
            if i == length or j == length:
                # print('i == length')
                return True
            if board[i][j] != '.':
                # print('board[i][j] == num')
                if j < length - 1:
                    newi = i
                    newj = j + 1
                else:
                    newi = i + 1
                    newj = 0

                return dfs(board,newi,newj, length)
            sectionNumber = i //3 * 3 + j//3
            used = [False] * 10
            for a in range(length):
                if board[a][j] != '.':
                    usednum = int(board[a][j])
                    if not used[usednum]:
                        used[usednum] = True
            for b in range(length):
                if board[i][b] != '.':
                    usednum = int(board[i][b])
                    if not used[usednum]:
                        used[usednum] = True
            
            for c in range(length):
                x = sectionNumber // 3 * 3 + c // 3
                y = sectionNumber % 3 * 3 + c % 3
                s = board[x][y]
                # print('xy',x,y)
                if s != '.':
                    usednum = int(s)
                    if not used[usednum]:
                        used[usednum] = True
            
            if sum(used) == 9:
                # print('sum(used) == 9')
                return False
            
            # print(board[i])
            # print(used)

            for x in range(1,10):
                
                if used[x]:
                    continue
                # print('Try: ',i,j)
                board[i][j] = str(x)
                if j < length - 1:
                    newi = i
                    newj = j + 1
                else:
                    newi = i + 1
                    newj = 0

                if dfs(board,newi,newj, length):
                    return True
                else:
                    board[i][j] = '.'
            
            return False
        N = len(board)
        dfs(board,0,0, N)
        return board

if __name__ == '__main__':
    solu = Solution()
    # input_List =  [2]
    input_List = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    
    # input_List = [4,5,6,7,0,1,2]
    # input_aim = 0
    result = solu.solveSudoku(input_List)

    # while result:
    #     print(result.val)
    #     result = result.next
    output_Str = 'result = ' + str(result)
    print(output_Str)