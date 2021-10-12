# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 20:05:14 2021

@author: qizhe
"""

class Solution:
    def isNumber(self, s: str) -> bool:
        """
        读题
        1、没看出有什么难度，不知道在考啥？
        2、要分状态，状态中判断出错
        3、比如，句首状态可以是 + - 0 . ；句中状态可以是 0 e . ； 句末状态 ……
        
        测试
        1、改了一堆bug，这题再也别看了
        
        """
        N = len(s)
        if N==1:
            if s =='.' or s =='e' or s == 'E':
                return False
        numlist = [str(i) for i in range(10)]
        validlist = numlist + ['.','+','-','e','E']
        # print(numlist,validlist)
        # state = 0
        dotFlag = 0
        signFlag = 0
        eFlag = 0
        numFlag = 0
        numCnt = 0
        for i in range(N):
            # 须为合法字符
            if s[i] not in validlist:
                # print('Error:',i)
                return False
            
            # 整数或小数的判断，最多有两个，最少有一个
            # 必须要统计数字个数
            if s[i] in numlist:
                # 新的数，是非连续数字，且不能是小数
                if not numFlag:    
                    numCnt +=1
                numFlag = 1
            else:
                if s[i] != '.':
                    numFlag = 0
            
            # 'e'处理
            if s[i] == 'e' or s[i] =='E':
                # 不多次出现 & e前必须有数字 & e后必须为整数
                if eFlag or i == N-1 or i == 0:
                    return False
                eFlag = 1
            # 符号处理
            if s[i] == '+' or s[i] == '-':
                # 重复出现
                if signFlag:
                    # 只有一种情况，就是前面有个e
                    if not (s[i-1] == 'e' or s[i-1] == 'E'):
                        # print('Error:',s,s[i-1],s[i])
                        return False
                else:
                    # 第一次出现，如果不在句首，那么前面必须要有e
                    if i != 0 and s[i-1] != 'e' and s[i-1] != 'E':
                        # print('Error:',s,s[i-1],s[i])
                        return False
                signFlag = 1
            # '.'处理
            if s[i] == '.':
                # 不可重复出现'.' & 可出现在句尾 否则 下一位必须为数字
                if eFlag or dotFlag or (i != N-1 and s[i+1] not in numlist and s[i+1]!='e' and s[i+1] != 'E'):
                    # print('Error:',s,dotFlag,i,s[i])
                    return False
                
                dotFlag = 1
        
        if numCnt == 0 or numCnt > 2 or (eFlag and numCnt !=2):
            # print('Error:',s)
            return False
        # print(numCnt)
        return True
        
        
        
        
        
if __name__ == '__main__':
    solu = Solution()
    numTruelist=["3e+7", "46.e3", "0089", ".1", "-0.1", "+3.14", "4.", ".9", "2e10", "-90E3", "+6e-1", "53.5e93", "-123.456e789"]
    numFalselist=["+.","6+1","-90e-.3", "1e+", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
    for i in range(len(numFalselist)):
        input_Str = numFalselist[i]
        # input_List = []
        # input_List = TreeNode(2)
        # input_List.left = TreeNode(3)
        # input_List.right = TreeNode(3)
        # input_List.left.left = TreeNode(4)
        # input_List.left.left.left = TreeNode(4)
        # input_List.left.right = TreeNode(5)
        # input_List.right.left = TreeNode(5)
        # input_List.right.right = TreeNode(3)
    
        result = solu.isNumber(input_Str)
    
        # output_Str = 'result = ' + solu.intToRoman(input_int)
        output_Str = ' result = ' + str(result)
        print(output_Str)