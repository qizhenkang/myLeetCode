# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 17:15:32 2021

@author: qizhe
"""

class Solution:
    def solveNQueens(self, n: int):
        """
        典型的回溯问题
        读题目，他要的是，所有解，不是找到一个就可以
        
        做了三次才做出来
        
        第三个思路对了，但性能很差，想办法剪枝一下，感觉主要问题在于valid 的恢复上面
        答案：
        核心思路：
        1、答案搞了3个集合，也就是三个约束来构造，就很简单了，然后优化搞一个位运算
        2、还有思路是每次都判断一下，感觉这个不太好
        
        改进：
        用第一个思路，就改了几行，性能突飞猛进
        优化了一下位运算
        """

        
        # 第三次尝试 N皇后问题，本质上是一个回溯问题，然后要有一个 valid数组记录就可以了
        # 难点是，要找全，就意味着，所有情况都要考虑到
        # 回溯的思路：
        #   1、下一个可行位置，递归搜索，从而保证所有情况都考虑到，这是最关键的一步
        #   2、感觉难点是，如何处理valid数组的复原问题
        def dfs(n,result,current,invalid,i):
            if len(current) == n:
                # 找到新答案，加入集合
                resultStr = ['']*n 
                for i in range(n):
                    temp = ['.'] * n
                    temp[current[i][1]] = 'Q'
                    resultStr[i] = ''.join(temp)
                result.append(resultStr)
                return
            if i >= n:
                return 
            # 只在这一行搜就可以了
            for y in range(n):
                if not invalid[0] >> y & 0b1 and not invalid[1] >> y+i & 0b1 and not invalid[2] >> y-i + n & 0b1 :
                    # 更新valid数组 只需要更新的是 左斜下方，正下方，右斜下方
                    invalid[0] |= 0b1 << y
                    invalid[1] |= 0b1 << y+i
                    invalid[2] |= 0b1 << y-i + n
                    dfs(n,result,current+[[i,y]],invalid,i+1)
                    invalid[0] &= ~(0b1 << y)
                    invalid[1] &= ~(0b1 << y+i)
                    invalid[2] &= ~(0b1 << y-i + n)
            return
        
        result = []
        current = []
        # 位运算改进
        invalid = [0,0,0]
        dfs(n,result,current,invalid,0)
        
        return result

if __name__ == '__main__':
    solu = Solution()
    
    input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    input_List = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    # input_List = 1

    result = solu.solveNQueens(5)

    output_Str = ' result = ' + str(result)
    print(output_Str)
