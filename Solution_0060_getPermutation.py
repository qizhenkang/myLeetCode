# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 10:06:44 2021

@author: qizhe
"""

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        读题：
        1、感觉像是一个全排列的问题，然后考虑排列顺序，以大小排列
        2、暴力解法是，全排列写出来，然后排序，找第k个，但太暴力了，显然时空都复杂
        3、简单解法，感觉上是，手动模拟从前之后计算，计算k次停止，空间复杂度显然很小
        4、好像 低位的组合次数，是一种全排列，阶乘
        5、是不是应该是回溯算法的提前终止，超时间了
        6、最后还是找规律了，利用阶乘进行逐级判断
        
        """
        
        # def dfs(result,current,used,n,k,cnt):
        #     print(current)
        #     if len(result) == k:
        #         return
        #     if len(current) == n:
        #         result.append(current)
        #         return
            
        #     for i in range(1,n+1):
        #         # 这里保证了从小到大
        #         if used[i]:
        #             continue
        #         used[i] = True
        #         dfs(result,current + str(i),used,n,k,cnt)
        #         used[i] = False
                
        #         if len(result) == k:
        #             break

        #     return
        
        # result = []
        # current = ''
        # cnt = 0
        # used = [False]*(n+1)
        # dfs(result,current,used,n,k,cnt)
        # return result[k-1]
        
        numlist = []
        # 形成初始字符串
        for i in range(1,n+1):
            numlist += [i]
        # print(numlist)
        result = ''
        multilist = [1]*(n+1)
        for i in range(1,n+1):
            multilist[i] = multilist[i-1] * i
        # print(multilist)
        # 本质思路是，当前位+1 则 次数 + multilist[x-1]次
        # 从前向后判断，从第n位，到第1位
        for x in range(n,0,-1):
            nowk = k
            nowNum = 1
            # 看该位可以有几个
            while nowk > multilist[x-1]:
                nowk -= multilist[x-1]
                nowNum += 1
            k = nowk 
            result += str(numlist[nowNum-1])
            numlist.pop(nowNum-1)
            # print(nowNum)
        
        return result
        
        # # 从前向后判断，从第n位，到第1位
        # for x in range(n,0,-1):
        #     # 首先判断当前位的剩余情况
        #     if k == 1:
        #         for x in numlist:
        #             result += str(x)
        #         break
        #     for i in range(1,n+1):
        #         # pass
        #         if k < multilist[i]:
        #             break
        #     # print(k, multilist[i],i)
        #     # print(i,k // multilist[i-1],numlist)
            
        #     # if k % multilist[i-1]:
        #     currNum = numlist[k // multilist[i-1]]
        #     result += str(currNum)
        #     numlist.pop(k // multilist[i-1])
        #     k %= multilist[i-1]
        #     # else:
        #     #     # print(x,k,i,multilist[i-1])
        #     #     currNum = numlist[k // multilist[i-1]]
        #     #     result += str(currNum)
        #     #     for x in numlist:
        #     #         result += str(x)
        #     #     break
                
            
        #     # print(x, k,cnt,k % cnt)
        #     # A为当前位，B为剩余
        #     # if x <= k:
        #     #     A = numlist[k // cnt]
        #     #     numlist.pop(k // cnt)
        #     #     k = k % cnt
        #     # else:
        #     #     A = numlist[0]
        #     #     numlist.pop(0)
        #     #     k = k % cnt
            
        #     # result += str(A)
        #     # print(A,k,result,numlist)
            
            
        # return result
        
    
if __name__ == '__main__':
    solu = Solution()
    
    # input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    # input_List = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    # s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    s = "AAAAAAAAAAAAA"
    # intervals = [[1,1],[3,5],[6,7],[8,10],[12,16]]
    # newInterval = [2,17]
    # intervals = [[2,5]]
    # newInterval = [5,7]
    # input_List = 1
    # numerator = -50
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    # for k in range(1,2):
    n = 3
    k = 1
    
    result = solu.getPermutation(n,k)
    
    output_Str = ' result = ' + str(n) + ' ' + str(k) + ' ' + str(result) 
    print(output_Str)