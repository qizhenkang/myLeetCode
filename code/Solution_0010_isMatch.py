# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:01:57 2021

@author: qizhe
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        读题：
        1、二次读题，就两个特殊字符嘛.和*，想起来不难嘛
        2、要求是：
            1 '.' 代表一个 任意 字符
            2 '*' 代表 0 - n 个 前面字符
            3 '.*' 代表 0 - n 个 任意字符
        3、记得答案是动态规划，如何解题呢？
        4、总觉得讨论一下就能解出来呢？
        5、带'*'号之后就很麻烦了，牵扯到一个像是“回溯”的问题，动态规划能解吗？
        6、感觉可以回溯来解呢，我试试
        
        测试：
        1、回溯写出来了，一次通过，但是性能比较特殊，内存占用很小，时间慢
        2、也就是说，回溯的方法没有用到 DP的大内存，但剪枝不够
        
        答案思路：
        1、这题看答案也看不懂，就仔细整理一下吧
        2、本质上是动态规划，难点在于'*'号的处理
        3、自己写一下动态规划，本质上就是 s 的前i 个和 p的前j 个匹配
        4、是一种记忆化搜索，充分利用前述的搜索结果
        
        答案重写测试：
        1、重写了很多次，通过了，还是不是非常理解
        """
        m = len(s)
        n = len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(m+1):
            for j in range(n+1):
                # 如果 j是0 必不行，dp[0][0] = True 已经提前考虑了
                if j == 0:
                    continue
                if p[j-1] == '*':
                    # 如果是 '*' 就复杂了，先看直接去掉是不是匹配
                    dp[i][j] |= dp[i][j-2] if j > 1 else i == 0
                    # 再看是否匹配，若匹配就和前述一致
                    if p[j-2] == '.'  or i != 0 and s[i-1] == p[j-2]:
                        dp[i][j] |= dp[i-1][j] if i > 0 else False
                else:
                    # 如果不是 '*' 就看是否匹配 匹配就与之前有关
                    if p[j-1] == '.'  or i > 0 and s[i-1] == p[j-1]:
                        dp[i][j] |= dp[i-1][j-1] if i > 0 else False

        
        return dp
        # m, n = len(s), len(p)
        
        # def matches(i: int, j: int) -> bool:
        #     if i == 0:
        #         return False
        #     if p[j - 1] == '.':
        #         return True
        #     return s[i - 1] == p[j - 1]
    
        # f = [[False] * (n + 1) for _ in range(m + 1)]
        # f[0][0] = True
        # for i in range(m + 1):
        #     for j in range(1, n + 1):
        #         if p[j - 1] == '*':
        #             f[i][j] |= f[i][j - 2]
        #             if matches(i, j - 1):
        #                 f[i][j] |= f[i - 1][j]
        #         else:
        #             if matches(i, j):
        #                 f[i][j] |= f[i - 1][j - 1]
        # return f


        # def dfs(s,p,spointer,ppointer,sLength):
        #     print(spointer,ppointer,s[spointer:],p[ppointer:])
        #     if spointer == sLength and ppointer == len(p):
        #         return True
        #     elif spointer == sLength:
        #         while ppointer < len(p) - 1 and p[ppointer +1] == '*':
        #             ppointer += 2
        #         if ppointer == len(p):
        #             return True
        #         else:
        #             return False
        #     elif ppointer == len(p):
        #         return False
            
        #     result = False
        #     if ppointer < len(p) - 1 and p[ppointer + 1] == '*':
        #         if p[ppointer] == '.':
        #             # 最麻烦的 '.*' 没有好办法
        #             # 一个一个试 这里可以剪枝
        #             # x = sLength - spointer
        #             # while not result and x >=0:
        #             #     result |= dfs(s,p,spointer+x,ppointer+2,sLength)
        #             #     x -= 1
        #             x = 0
        #             while not result and x <= sLength - spointer:
        #                 result |= dfs(s,p,spointer+x,ppointer+2,sLength)
        #                 x -= 0
        #         else:
        #             # 'A*'处理
        #             # 这里可以剪枝
        #             cutFlag = 0
        #             x = 0
        #             while not result and x < sLength - spointer and s[spointer+x] == p[ppointer]:
        #                 result |= dfs(s,p,spointer+x,ppointer+2,sLength)
        #                 x +=1
        #             result |= dfs(s,p,spointer+x,ppointer+2,sLength)
        #     else:  # 单独一个'.'
        #         if p[ppointer] == '.' or p[ppointer] == s[spointer]:
        #             result |= dfs(s,p,spointer+1,ppointer+1,sLength)

        #     return result

        # return dfs(s,p,0,0,len(s))



if __name__ == '__main__':
    solu = Solution()
    # input_numRows = 2
    # input_Str_s = str('aab')
    # input_Str_p = str('.*a*b')
    # input_Str_s = str('aab')
    # input_Str_p = str('b.*')
    
    input_Str_s = "aaacd"
    input_Str_p = "a*aaaacd"
    input_Str_s = str('mississippi')
    input_Str_p = str('mis*is*p*.')
    
    input_Str_s = str('abcdef')
    input_Str_p = str('.*f')
    
    # input_Str_s = str('a')
    # input_Str_p = str('a*b*c*')
    
    input_Str_s = str('aa')
    input_Str_p = str('a')
    result = solu.isMatch(input_Str_s, input_Str_p)
    for i in result:
        print(i)
    
    # output_Str = 'result = ' + str(result)
    # print(output_Str)
