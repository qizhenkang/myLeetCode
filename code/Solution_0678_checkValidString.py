# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:18:42 2021

@author: qizhe
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # 建立两个栈，是问题的关键
        # 左括号栈/星号栈
        stackleft = []
        stackstar = []
        
        # 注意，栈内存的是下标，为了后面判断左括号与星号用
        for i in range(len(s)):
            if s[i] == '(':
                stackleft.append(i)
            elif s[i] == '*':
                stackstar.append(i)
            elif s[i] == ')':
                # 保证左括号栈不为空
                if stackleft:
                    stackleft.pop()
                    continue
                
                # 若左括号栈为空，则应该有星号来作为左括号
                if stackstar:
                    stackstar.pop()
                    continue
                
                # 若星号栈也为空，则返回错误
                return False
        
        # 若执行结束，还有左括号，那星号应该补充为右括号，且星号下标应该大于左括号
        for i in stackleft[::-1]:
            if stackstar:
                if i < stackstar.pop():
                    continue
                else:
                    print(i)
                    return False
            else:
                return False
        # if len(stackleft) > len(stackstar):
        #     return False
        
        return True
            
            
            
if __name__ == '__main__':
    solu = Solution()

    input_Str = str('(()()*)(*))')
    input_Str = str('()(())(((((()())(()))))()(*()))()()()()((()(())())*((((())))*())()(()()))*((()(()(()))))(()())(*(*')
    # input_Str = str('(()()*)(*))')
    # input_List =[[0,0],[1,0],[2,0]]
    # input_List = TreeNode(1)
    # input_List.left = TreeNode(2)
    # input_List.right = TreeNode(3)
    
    result = solu.checkValidString(input_Str)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)