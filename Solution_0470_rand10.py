# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 14:43:17 2021

@author: qizhe
"""

import random
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self,n=1):
        """
        :rtype: int
        """

        def rand7():
            return random.randint(1,7)
        
        while True:
            
            row = rand7()
            col = rand7()
            
            idx = (row-1) * 7 + col
            print(row,col,idx)
            if idx <= 40: 
                return (idx - 1) % 10 + 1
        

if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    input_List = []
    # input_List = TreeNode(2)
    # input_List.left = TreeNode(3)
    # input_List.right = TreeNode(3)
    # input_List.left.left = TreeNode(4)
    # input_List.left.left.left = TreeNode(4)
    # input_List.left.right = TreeNode(5)
    # input_List.right.left = TreeNode(5)
    # input_List.right.right = TreeNode(3)

    result = solu.rand10()

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)