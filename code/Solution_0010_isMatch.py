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
        """
        
        def dfs(s,p,spointer,ppointer,sLength):
            print(spointer,ppointer,s[spointer:],p[ppointer:])
            if spointer == sLength and ppointer == len(p):
                return True
            elif spointer == sLength:
                while ppointer < len(p) - 1 and p[ppointer +1] == '*':
                    ppointer += 2
                if ppointer == len(p):
                    return True
                else:
                    return False
            elif ppointer == len(p):
                return False
            
            result = False
            if ppointer < len(p) - 1 and p[ppointer + 1] == '*':
                if p[ppointer] == '.':
                    # 最麻烦的 '.*' 没有好办法
                    # 一个一个试 这里可以剪枝
                    # x = sLength - spointer
                    # while not result and x >=0:
                    #     result |= dfs(s,p,spointer+x,ppointer+2,sLength)
                    #     x -= 1
                    x = 0
                    while not result and x <= sLength - spointer:
                        result |= dfs(s,p,spointer+x,ppointer+2,sLength)
                        x -= 0
                else:
                    # 'A*'处理
                    # 这里可以剪枝
                    cutFlag = 0
                    x = 0
                    while not result and x < sLength - spointer and s[spointer+x] == p[ppointer]:
                        result |= dfs(s,p,spointer+x,ppointer+2,sLength)
                        x +=1
                    result |= dfs(s,p,spointer+x,ppointer+2,sLength)
            else:  # 单独一个'.'
                if p[ppointer] == '.' or p[ppointer] == s[spointer]:
                    result |= dfs(s,p,spointer+1,ppointer+1,sLength)

            return result
        

        return dfs(s,p,0,0,len(s))
        # spointer = 0
        # ppointer = 0
        # N = len(s)
        # while ppointer < N:
        #     # 处理'*'
        #     if ppointer < N - 1 and p[ppointer + 1] == '*':
        #         if p[ppointer] == '.':
        #             # 最麻烦的 '.*' 没有好办法
        #         else:
        #             # 'A*'处理
        #             if ppointer + 1 < N - 1
        #             while s[spointer] == p[ppointer] or s[spointer] == p[ppointer+2]:
        #                 spointer += 1
        #     else:  # 单独一个'.'
        #         if p[ppointer] == '.' or p[ppointer] == s[spointer]:
        #             spointer += 1
        #             ppointer += 1
        #         else:
        #             return False

        # return result


if __name__ == '__main__':
    solu = Solution()
    # input_numRows = 2
    # input_Str_s = str('aab')
    # input_Str_p = str('.*a*b')
    
    input_Str_s = "aaacd"
    input_Str_p = "a*aaaacd"
    # input_Str_s = str('mississippi')
    # input_Str_p = str('mis*is*p*.')
    
    # input_Str_s = str('abcdef')
    # input_Str_p = str('ab.*f')
    
    # input_Str_s = str('a')
    # input_Str_p = str('a*b*c*')
    
    # input_Str_s = str('aa')
    # input_Str_p = str('a')
    
    output_Str = 'result = ' + str(solu.isMatch(input_Str_s, input_Str_p))
    print(output_Str)
