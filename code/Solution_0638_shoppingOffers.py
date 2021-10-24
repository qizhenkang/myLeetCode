# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 09:42:31 2021

@author: qizhe
"""
from typing import List
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        """
        读题：
        1、有点像“背包”问题，首先考虑动态规划
        2、最终目标是价格最小，优先考虑大礼包，然后用单价填满
        3、特殊规则是，只能买正好的，不能买多了，这样应该是简化了
        4、感觉是一种暴力搜索呢？感觉不知道该怎么办，好像是一种组合问题
        5、回溯怎么样呢？
        
        测试：
        1、用回溯，一次通过，性能不错，做了40min
        
        答案：
        1、确实高级一些，还没来得及仔细看
        """
        def __dfs(price,special,needs,result,currentPrice,currentNeeds,needlength,maxprice):
            if currentPrice > maxprice:
                return 
            nowPrice = currentPrice
            for i in range(needlength):
                nowPrice += currentNeeds[i] * price[i]
            result[0] = min(result[0],nowPrice)
            # print(currentPrice,nowPrice,currentNeeds)
            for sp in special:
                nextNeeds = [0] * needlength
                okFlag = 1
                for j in range(needlength):
                    nextNeeds[j] = currentNeeds[j] - sp[j]
                    if nextNeeds[j] < 0:
                        okFlag = 0
                        break
                if okFlag:
                    __dfs(price,special,needs,result,currentPrice + sp[needlength],nextNeeds,needlength,maxprice)
            
            return
        N = len(needs)
        maxprice = 0
        for i in range(N):
            maxprice += price[i]* needs[i]
        result = [maxprice]
        currentPrice = 0
        currentNeeds = needs
        __dfs(price,special,needs,result,currentPrice,currentNeeds,N,maxprice)

        return result[0]
    
    
if __name__ == '__main__':
    solu = Solution()

    # nums = [3,2,1,5]

    n = 8
    inputList = [1]
    inputList = [2, 0, 5, 6, 2, 3]
    matrix = [["0","1","0","1","0"],["1","1","0","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    matrix = []
    matrix = [["0"],['1']]
    matrix = [["1","0"]]
    ss = ['12',"23",'20310','06','011106','111111111111111111111111111111111111111111111']
    ss = ['1234','2101','123123']
    area = [1,2,80,100000,10000000]
    # for s in range(8):
    price = [2,5]
    special = [[3,0,5],[1,2,10]]
    needs = [3,2]
    # price = [2,3,4]
    # special = [[1,1,0,4],[2,2,1,9]]
    # needs = [1,2,1]
    result = solu.shoppingOffers(price, special, needs)

    output_Str = ' result = ' + str(result)
    print(output_Str)
    