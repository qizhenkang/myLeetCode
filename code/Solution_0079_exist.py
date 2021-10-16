# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 18:12:27 2021

@author: qizhe
"""

class Solution:
    def exist(self, board, word: str) -> bool:
        """
        读题：
        1、感觉不难，就是一个暴力搜索 - 回溯
        2、基本思路是：先找起点，然后从起点开始回溯
        3、找起点：顺序搜索，找到所有起点
        4、回溯：一个一个地试试
        5、有没有可能剪枝，尽可能地加速搜索
        
        测试：
        1、一次通过，性能很好
        
        """
        def dfs(board,word,wordpointer,i,j,unused):
            
            if wordpointer >= len(word):
                return True
            
            result = False
            if i < len(board) - 1 and unused[i+1][j] and board[i+1][j] == word[wordpointer]:
                unused[i+1][j] = False
                result |= dfs(board,word,wordpointer+1,i+1,j,unused)
                unused[i+1][j] = True
            if not result and i > 0 and unused[i-1][j] and board[i-1][j] == word[wordpointer]:
                unused[i-1][j] = False
                result |= dfs(board,word,wordpointer+1,i-1,j,unused)
                unused[i-1][j] = True
            if not result and j < len(board[0]) - 1 and unused[i][j+1] and board[i][j+1] == word[wordpointer]:
                unused[i][j+1] = False
                result |= dfs(board,word,wordpointer+1,i,j+1,unused)
                unused[i][j+1] = True
            if not result and j > 0 and unused[i][j-1] and board[i][j-1] == word[wordpointer]:
                unused[i][j-1] = False
                result |= dfs(board,word,wordpointer+1,i,j-1,unused)
                unused[i][j-1] = True

            return result
        
        m = len(board)
        n = len(board[0])
        unused = [[True] * n for _ in range(m)]
        result = False
        for i in range(m):
            for j in range(n):
                unused = [[True] * n for _ in range(m)]
                if board[i][j] == word[0]:
                    unused[i][j] = False
                    result |= dfs(board,word,1,i,j,unused)
                if result:
                    break

        return result
        

if __name__ == '__main__':
    solu = Solution()
    
    word1 = "horse"
    
    word2 = 'ros'
    # arr = '/home//foo/'
    # arr = '/../'
    nums = [0]
    # input_List = 1
    # s = "ADOBECODEBANC"
    # t = "ABC"
    # s = 'bacd'
    # t = 'cd'
    num = "105"
    target = 5
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "CCESEEFBASA"

    result = solu.exist(board,word)

    output_Str = ' result = ' + str(result)
    print(output_Str)
