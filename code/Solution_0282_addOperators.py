# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 09:13:46 2021

@author: qizhe
"""

class Solution:
    def addOperators(self, num: str, target: int):
        """
        读题：
        1、感觉最简单就是暴力回溯
        2、能不能剪枝，比如每个空格其实有4种选择： ' ' or '+' or '-' or '*'
        3、是不是有一定的大小顺序？
        
        不会做了，看答案
        
        答案：
        1、核心的思路仍然是暴力回溯
        2、不太一样的是，他是先确定数字划分，再进行 + - *的回溯
        3、乘法是特殊的，他要撤销前一次的计算
        
        我还不太会
        """

        n = len(num)
        ans = []

        def backtrack(expr, i: int, res: int, mul: int):
            # 终止条件
            if i == n:
                if res == target:
                    ans.append(''.join(expr))
                return
            signIndex = len(expr)
            if i > 0:
                expr.append('')  # 占位，下面填充符号
            val = 0
            # 枚举截取的数字长度（取多少位）
            for j in range(i, n):  
                # 数字可以是单个 0 但不能有前导零
                if j > i and num[i] == '0': 
                    break
                val = val * 10 + int(num[j])
                expr.append(num[j])
                # 表达式开头不能添加符号
                if i == 0:  
                    backtrack(expr, j + 1, val, val)
                else:  
                    # 枚举符号
                    expr[signIndex] = '+'; backtrack(expr, j + 1, res + val, val)
                    expr[signIndex] = '-'; backtrack(expr, j + 1, res - val, -val)
                    expr[signIndex] = '*'; backtrack(expr, j + 1, res - mul + mul * val, mul * val)
            del expr[signIndex:]

        backtrack([], 0, 0, 0)
        return ans


        # def dfs(num,target,result,current,currenttarget,depth):
            
        #     if depth == len(num) - 1:
        #         # if currenttarget == target:
        #         numstack = []
        #         opstack = []
        #         numFlag = 0
        #         num = 0
        #         i = 0
        #         while i < len(current) - 1:
        #             if current[i] == '+' or current[i] == '-':
        #                 opstack.append(current[i])
        #                 numFlag = 0
        #                 continue
        #             if current[i] == '*':
        #                 calcu = current[i+1] * numstack.pop()
        #                 # i +=
                        
        #             if numFlag:
        #                 if not ():
        #                     num = num*10 + current[i]
        #             else:
        #                 num = current[i]
        #                 numFlag = 1
        #             i += 1
                    
        #         result.append(current+num[depth])
                
        #         return
            
        #     dfs(num,target,result,current + num[depth] + '-',currenttarget,depth+1)
        #     dfs(num,target,result,current + num[depth] + '+',currenttarget,depth+1)
        #     dfs(num,target,result,current + num[depth] + '*',currenttarget,depth+1)
        #     dfs(num,target,result,current + num[depth] + '',currenttarget,depth+1)
            
        #     return
        # result = []

        # dfs(num,target,result,'',0,0)
        # return result

    
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

    result = solu.addOperators(num,target)

    output_Str = ' result = ' + str(result)
    print(output_Str)


        