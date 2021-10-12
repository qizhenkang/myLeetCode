# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 14:54:30 2021

@author: qizhe
"""

class Solution:
    def isValidSudoku(self, board) -> bool:
        """
        不是让你解数独，而是只是看看有没有明显错误（所谓的“有效”）
        答案写的挺好的，有用哈希表的，有用数组的
        感觉最好的是位运算，实现一下

        """
        # print(board)
        row = [int(0)] * 9
        col = [int(0)] * 9
        box = [int(0)] * 9
        for i in range(9):
            
            for j in range(9):
                
                sectionNumber = int(j//3 + (i//3) * 3)
                # if (j/3 + i) - sectionNumber == 0:
                #     print(i,j)
                
                
                if board[i][j] == '.':
                    continue
                val = int(board[i][j])
                # print(val,board[i][j])
                if row[i] >> val & 0b1 or col[j] >> val & 0b1 or box[sectionNumber] >> val & 0b1:
                    # print(i,j,val,bin(row[i]),bin(col[j]),bin(box[sectionNumber]))
                    # print(i,j,val,bin(row[i]>>val),bin(col[j]>>val),bin(box[sectionNumber]>>val))
                    return False
                
                row[i] |= 1 << val
                col[j] |= 1 << val
                box[sectionNumber] |= 1 << val

        
        return True
    

if __name__ == '__main__':
    solu = Solution()
    
    # input_List = [1,6,5,4,3,2,1]
    
    input_List =[["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

    result = solu.isValidSudoku(input_List)

    output_Str = ' result = ' + str(result)
    print(output_Str)