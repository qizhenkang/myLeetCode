# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 14:19:50 2021

@author: qizhe
"""
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且
# 有效的 括号组合。
#
# 现在还有错误，123 124 133 134 144 序列不会生成


class Solution:
    def generateParenthesis(self, n: int):
        """
        典型的回溯问题
        8月14 一开始完全不懂怎么做，在找规律啥的
        9月30 学了回溯算法之后，基本是几分钟就写完了
        本质上是DFS的暴力搜索，然后剪枝
        """
        def dfs(n,current,result,leftNum,rightNum):
            if leftNum + rightNum == 2*n:
                result.append(current)
                return
            if leftNum < n:
                dfs(n,current + '(',result,leftNum+1,rightNum)
            if rightNum < leftNum:
                dfs(n,current + ')',result,leftNum,rightNum+1)
            
            return

        # depth = 2 * n
        current = ''
        result = []
        dfs(n,current,result,0,0)
        return result

    #     # 右括号插入位置列表
    #     num_list = list(range(1, n+1))
    #     result = []

    #     # 所有数字向右移动至n，
    #     # 即从1234，到1244，……到4444
    #     for h in range(1, n+1):
    #         for i in range(h):
    #             num_list[i] = h
    #         result.append(self.generatelist(num_list, n))

    #         for i in range(n-2, 0, -1):
    #             while(num_list[i] < n):
    #                 num_list[i] = num_list[i] + 1
    #                 result.append(self.generatelist(num_list, n))

    #     return result

    # # def generateNum(self, num_list, n, k):

    # #     # if k <= 0:
    # #     #     return

    # #     # if num_list[k] < n:
    # #     #     num_list[k] = num_list[k] + 1
    # #     # else:
    # #     #     num_list[k]
    # #     # return num_list

    # #     # for i in range(n):

    # #     #     num_list = self.generateNum(self, num_list, n, k-1)

    # #     return num_list

    # def generatelist(self, num_list, n):
    #     leftstr_list = list('('*n)
    #     for i in range(n-1, -1, -1):
    #         leftstr_list.insert(num_list[i], ')')
    #     return ''.join(leftstr_list)


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('{[]{}()}')
    # input_list =
    input_List = [90]
    input_int = 3

    result = solu.generateParenthesis(input_int)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(result)
    print(output_Str)
