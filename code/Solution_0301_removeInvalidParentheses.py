# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 09:41:15 2021

@author: qizhe
"""

from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        读题：
        1、括号匹配本身就是栈
        2、求所有组合是回溯
        3、所以，回溯必然能做，我想试试迭代DFS
        4、字母完全没用，就是干扰你的
        5、开始做的时候发现，判断是否匹配简单，但判断删除是一件很复杂的事，必然是要大量搜索
        6、搜索时候，就要判断是否有必要往前走
        7、要删除最少括号，必然只删除一种括号（这里错了，没考虑末尾的(）
        
        测试：
        1、错误两次通过，错了一个leftrightFlag的设计，性能良好
        2、回溯的特点总是这样，内存占用小，但用时高
        
        答案：
        1、基本思路没问题，答案也是回溯/BFS/枚举
        2、广度优先搜索好像更适用
        """
        def __dfs(s,result,current,currentValue,now,deleteNum):
            # print(current,deleteNum)
            if now == len(s):
                if currentValue == 0 and current not in result:
                    result.append(current)
                return

                
            if s[now] != '(' and s[now] != ')':
                __dfs(s,result,current+s[now],currentValue,now+1,deleteNum)
                return

            # 右括号，要判断合法性
            if s[now] == ')' and currentValue <= 0:
                # 右括号不合法，必然是只能删除，这时候就不管flag了，保持即可
                if deleteNum > 0: 
                    __dfs(s,result,current,currentValue,now+1,deleteNum-1)
            else:
                # 合法就有两种情况
                if s[now] == '(':
                    __dfs(s,result,current+'(',currentValue+1,now+1,deleteNum) # 保持
                    if deleteNum >0 :
                        __dfs(s,result,current,currentValue,now+1,deleteNum-1) # 删除了左括号，写-1
                else:
                    __dfs(s,result,current+')',currentValue-1,now+1,deleteNum) # 保持
                    if deleteNum >0 :
                        __dfs(s,result,current,currentValue,now+1,deleteNum-1) # 删除了右括号，写+1
            
            
            return
        deleteNum = 0
        balance = 0
        for i in range(len(s)):
            if s[i] == '(':
                balance += 1
            elif s[i] == ')':
                if balance <= 0:
                    deleteNum += 1
                else:
                    balance -= 1
        
        deleteNum += balance
        # print(deleteNum,balance)
        result = []
        # if deleteNum:
        __dfs(s,result,'',0,0,deleteNum)

        return result

if __name__ == '__main__':
    solu = Solution()
    # input_numRows = 2
    # input_Str_s = str('aab')
    # input_Str_p = str('.*a*b')
    
    s = "a)())("
    # s = "n"
    # s = ")(()c))("

    
    output_Str = 'result = ' + str(solu.removeInvalidParentheses(s))
    print(output_Str)
