# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:24:08 2021

@author: qizhe
"""

class StockPrice:
    
    """
    超时了
    """

    def __init__(self):
        self.time = []
        self.value = []
        self.maxPrice = 0
        self.secondmaxPrice = 0
        self.minPrice = 0
        self.secondminPrice = 0
        self.maxChangeFlag = 0
        self.minChangeFlag = 0
        return


    def update(self, timestamp: int, price: int):
        
        if not self.time:
            self.maxPrice = price
            self.secondmaxPrice = price
            self.minPrice = price
            self.secondminPrice = price
        else:
            if price > self.maxPrice:
                self.secondmaxPrice = self.maxPrice
                self.maxPrice = price
            if price < self.minPrice:
                self.secondminPrice = self.minPrice
                self.minPrice = price
                
        enterFlag = 0
        for i in range(len(self.time)):
            if timestamp == self.time[i]:
                oldValue = self.value[i]
                self.value[i] = price
                self.changeFlag = 1
                if oldValue == self.maxPrice:
                    self.maxChangeFlag = 1
                #     if oldValue != self.secondmaxPrice:
                #         self.maxPrice = self.secondmaxPrice
                #     else:
                #         self.maxPrice = max(self.value)
                if oldValue == self.minPrice:
                    self.minChangeFlag = 1
                #     if oldValue != self.secondminPrice:
                #         self.minPrice = self.secondminPrice
                #     else:
                #         self.minPrice = min(self.value)
                enterFlag = 1
                break
            if self.time[i] > timestamp:
                self.time.insert(i, timestamp)
                self.value.insert(i, price)
                enterFlag = 1
                break
            
        if not enterFlag:
            self.time.append(timestamp)
            self.value.append(price)
        
        return


    def current(self) -> int:
        return self.value[-1]


    def maximum(self) -> int:
        if self.maxChangeFlag:
            self.maxChangeFlag = 0
            self.maxPrice = max(self.value)
        
        return self.maxPrice


    def minimum(self) -> int:
        if self.minChangeFlag:
            self.minChangeFlag = 0
            self.minPrice = min(self.value)
        
        return self.minPrice



# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

if __name__ == '__main__':
    stockPrice = StockPrice()

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
    
    stockPrice.update(85, 4908) #时间戳为 [1] ，对应的股票价格为 [10] 。
    stockPrice.update(85, 5125) #时间戳为 [1] ，对应的股票价格为 [10] 。
    
    
    stockPrice.update(2, 5)# 时间戳为 [1,2] ，对应的股票价格为 [10,5] 。
    x1 = stockPrice.current()# 返回 5 ，最新时间戳为 2 ，对应价格为 5 。
    x2 = stockPrice.maximum()# 返回 10 ，最高价格的时间戳为 1 ，价格为 10 。
    stockPrice.update(1, 3)# 之前时间戳为 1 的价格错误，价格更新为 3 。
                              # 时间戳为 [1,2] ，对应股票价格为 [3,5] 。
    x3 = stockPrice.maximum()# 返回 5 ，更正后最高价格为 5 。
    stockPrice.update(4, 2)# 时间戳为 [1,2,4] ，对应价格为 [3,5,2] 。
    x4 = stockPrice.minimum()# 返回 2 ，最低价格时间戳为 4 ，价格为 2 。

    print(x1,x2,x3,x4)
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