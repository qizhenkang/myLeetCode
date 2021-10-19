# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 10:40:03 2021

@author: qizhe
"""

class Bank:

    def __init__(self, balance):
        
        self.money = [0] + balance
        self.length = len(balance)
        return


    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 <= self.length and account2 <= self.length and self.money[account1] >= money:
            self.money[account1] -= money
            self.money[account2] += money
            return True
        else:
            return False


    def deposit(self, account: int, money: int) -> bool:
        if account <= self.length:
            self.money[account] += money
            return True
        else:
            return False


    def withdraw(self, account: int, money: int) -> bool:
        if account <= self.length and self.money[account] >= money:
            self.money[account] -= money
            return True
        else:
            return False



# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)

# if __name__ == '__main__':
#     solu = Solution()
    
#     input_List = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
#     input_List = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
#     # input_List = 1
#     s = "hello world 5 x 5"
#     result = solu.areNumbersAscending(s)

#     output_Str = ' result = ' + str(result)
#     print(output_Str)