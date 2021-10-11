# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:24:08 2021

@author: qizhe
"""

# import heapq
from sortedcontainers import SortedList

class StockPrice:
    
    """
    答案：双百通过。
    利用了一个“容器”有序列表
    
    能不能自己维护一个有序列表？ 应该很简单吧？
    """
    def __init__(self):
        self.priceDict = {} # 用于记录时间-价格的哈希表
        self.pricesHistory = SortedList() # 用于记录历史价格的有序列表
        self.currentTime = 0 # 用于记录当前时间（最大时间）
        return


    def update(self, timestamp: int, price: int):
        self.currentTime = max(self.currentTime,timestamp)
        if timestamp in self.priceDict:
            self.pricesHistory.discard(self.priceDict[timestamp])
        self.pricesHistory.add(price)
        self.priceDict[timestamp] = price
        
        return


    def current(self) -> int:
        return self.priceDict[self.currentTime]


    def maximum(self) -> int:
        return self.pricesHistory[-1]


    def minimum(self) -> int:
        return self.pricesHistory[0]

if __name__ == '__main__':
    stockPrice = StockPrice()
    
    # stockPrice.update(1, 3)
    # stockPrice.update(3, 2)
    # stockPrice.update(2, 1)
    # print(stockPrice.priceDict)

    stockPrice.update(88, 9184) #时间戳为 [1] ，对应的股票价格为 [10] 。
    stockPrice.update(83, 343) #时间戳为 [1] ，对应的股票价格为 [10] 。
    stockPrice.update(87, 693) #时间戳为 [1] ，对应的股票价格为 [10] 。
    stockPrice.update(88, 7810) #时间戳为 [1] ，对应的股票价格为 [10] 。
    stockPrice.update(89, 624) #时间戳为 [1] ，对应的股票价格为 [10] 。
    stockPrice.update(86, 9963) #时间戳为 [1] ，对应的股票价格为 [10] 。
    stockPrice.update(88, 7345) #时间戳为 [1] ，对应的股票价格为 [10] 。
    stockPrice.update(83, 5533) #时间戳为 [1] ，对应的股票价格为 [10] 。
    x1 = stockPrice.current()# 返回 5 ，最新时间戳为 2 ，对应价格为 5 。
    x2 = stockPrice.maximum()# 返回 10 ，最高价格的时间戳为 1 ，价格为 10 。
    x3 = stockPrice.minimum()# 返回 2 ，最低价格时间戳为 4 ，价格为 2 。
    print(x1,x2,x3,x3)
    
    # stockPrice.update(85, 4908) #时间戳为 [1] ，对应的股票价格为 [10] 。
    # stockPrice.update(85, 5125) #时间戳为 [1] ，对应的股票价格为 [10] 。
    
    
    # stockPrice.update(2, 5)# 时间戳为 [1,2] ，对应的股票价格为 [10,5] 。
    # x1 = stockPrice.current()# 返回 5 ，最新时间戳为 2 ，对应价格为 5 。
    # x2 = stockPrice.maximum()# 返回 10 ，最高价格的时间戳为 1 ，价格为 10 。
    # stockPrice.update(1, 3)# 之前时间戳为 1 的价格错误，价格更新为 3 。
    #                           # 时间戳为 [1,2] ，对应股票价格为 [3,5] 。
    # x3 = stockPrice.maximum()# 返回 5 ，更正后最高价格为 5 。
    # stockPrice.update(4, 2)# 时间戳为 [1,2,4] ，对应价格为 [3,5,2] 。
    # x4 = stockPrice.minimum()# 返回 2 ，最低价格时间戳为 4 ，价格为 2 。

    # print(x1,x2,x3,x4)
    # Your StockPrice object will be instantiated and called as such:
    # obj = StockPrice()
    # obj.update(timestamp,price)
    # param_2 = obj.current()
    # param_3 = obj.maximum()
    # param_4 = obj.minimum()
    # result = solu.minOperations(grid, x)
    # output_Str = ' result = '
    # print(' result = ',end=' ')
    # while result:
    #     print(result.val,end=' ')
    #     result = result.next


    # output_Str = ' result = ' + str(result) 
    # print(output_Str)