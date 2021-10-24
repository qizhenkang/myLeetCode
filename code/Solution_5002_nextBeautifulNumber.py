# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 10:55:54 2021

@author: qizhe
"""


from typing import List
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # print(n)
        bit = 0
        num = n
        while num:
            num //=10
            bit +=1
        
        def dfs(result,current,currentbit,used,begin):
            if currentbit <0:
                return
            if currentbit == 0:
                result.append(current)
            for i in range(begin,10):
                if used[i]:
                    continue
                used[i] = True
                dfs(result,current+[i]*i,currentbit-i,used,i+1)
                used[i] = False
            return
        
        result = []
        used = [False] * 10
        dfs(result,[],bit,used,1)
        maxValue = 0
        for i in range(bit):
            maxValue *= 10
            maxValue += result[-1][bit-i-1]
        # print(n,maxValue)
        if n >= maxValue:
            result = []
            used = [False] * 10
            bit +=1
            dfs(result,[],bit,used,1)
            print(result)
            aimValue = 0
            for i in range(bit):
                aimValue *= 10
                aimValue += result[0][i]
        else:
            nlist = []
            # print(n)
            num = n
            for i in range(bit):
                nlist.append(num%10)
                num //= 10
            nlist = nlist[::-1]
            aimResultlist = -1
            for x in range(len(result)):
                remaxValue = 0
                for i in range(bit):
                    remaxValue *= 10
                    remaxValue += result[x][bit-i-1]
                print(n,x,remaxValue)
                if n < remaxValue:
                    aimResultlist = x
                    break
            resultlist = result[aimResultlist]
            # print(n,result)
            print(n,resultlist,aimResultlist)
            usedresult = [False] * bit
            aimValue = 0
            # xxresults = []
            # def xxx(resultlist,xxresults,current,usedresult,begin,bit):
            #     if begin == bit:
            #         xxresults.append(current)
            #         return
            #     for j in range(bit):
            #         if usedresult[j]:
            #             continue
            #         usedresult[j] = True
            #         xxx(resultlist,xxresults,current+[j],usedresult,begin+1,bit)
            #         usedresult[j] = False
            # xxx(resultlist,xxresults,[],usedresult,0,bit)
            # print(xxresults)
            lastaim = -1
            i = 0
            tuiFlag = 0
            while i < bit:
                print(i,tuiFlag)
                for j in range(bit):
                    if usedresult[j]:
                        continue
                    if resultlist[j] >= nlist[i] and not tuiFlag or tuiFlag and resultlist[j] >= nlist[i] +1:
                        aimValue += resultlist[j]
                        aimValue *= 10 
                        usedresult[j] = True
                        lastaim = j
                        tuiFlag = 0
                        break
                    if j == bit-1:
                        print('..')
                        i -= 2
                        tuiFlag = 1
                        usedresult[lastaim] = False
                        break
                i += 1
                        
            aimValue //= 10 
            print(aimValue)
                
        # 获得位数
        # if n
        # now
        # mylist = [1]
        # while True:
        #     for i in range()
        #     mylist.append()
        
        return aimValue

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
    nn = [1,188,1000,3000,99999,999999,1000000]
    for n in nn:
        result = solu.nextBeautifulNumber(n)
    
        output_Str = ' result = ' + str(result)
        print(output_Str)