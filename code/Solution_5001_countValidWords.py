# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 10:28:06 2021

@author: qizhe
"""
from typing import List
import string

class Solution:
    def countValidWords(self, sentence: str) -> int:
        senlist = sentence.split(' ')
        print(senlist)
        cnt = 0
        numlist = [str(i) for i in range(10)]
        numDict = set(numlist)
        fuSet = set(['!','.',','])
        for word in senlist:
            wordFlag = 1
            lianFlag = 1
            fuSetFlag = 1
            for i in range(len(word)):
                # if (word[i] in fuSet and (not fuSetFlag or i == len(word) -1)):
                #     print(word[i],i,word)
                if (word[i] in fuSet and (not fuSetFlag or i != len(word) -1)) or word[i] in numDict or word[i] == ' ' or (word[i] =='-' and (not lianFlag or i == 0 or i == len(word)-1)) or (i== 0 and len(word)>1 and word[i] not in string.ascii_lowercase) :
                    wordFlag = 0
                    break
                
                if fuSetFlag and word[i] in fuSet:
                    
                    fuSetFlag = 0
                if lianFlag and word[i] =='-':
                    if word[i+1] not in string.ascii_lowercase:
                        wordFlag = 0
                        break
                    lianFlag = 0
            # print(word,wordFlag)
            if wordFlag and len(word):
                cnt += 1
        return cnt
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
    ss = ["a-b.","afad","ba-c","a!" , "!","a-!b","cat and  dog", "!this  1-s b8d!", "alice and  bob are playing stone-game10", "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."]
    ss.append(" 62   nvtk0wr4f  8 qt3r! w1ph 1l ,e0d 0n 2v 7c.  n06huu2n9 s9   ui4 nsr!d7olr  q-, vqdo!btpmtmui.bb83lf g .!v9-lg 2fyoykex uy5a 8v whvu8 .y sc5 -0n4 zo pfgju 5u 4 3x,3!wl  fv4   s  aig cf j1 a i  8m5o1  !u n!.1tz87d3 .9    n a3  .xb1p9f  b1i a j8s2 cugf l494cx1! hisceovf3 8d93 sg 4r.f1z9w   4- cb r97jo hln3s h2 o .  8dx08as7l!mcmc isa49afk i1 fk,s e !1 ln rt2vhu 4ks4zq c w  o- 6  5!.n8ten0 6mk 2k2y3e335,yj  h p3 5 -0  5g1c  tr49, ,qp9 -v p  7p4v110926wwr h x wklq u zo 16. !8  u63n0c l3 yckifu 1cgz t.i   lh w xa l,jt   hpi ng-gvtk8 9 j u9qfcd!2  kyu42v dmv.cst6i5fo rxhw4wvp2 1 okc8!  z aribcam0  cp-zp,!e x  agj-gb3 !om3934 k vnuo056h g7 t-6j! 8w8fncebuj-lq    inzqhw v39,  f e 9. 50 , ru3r  mbuab  6  wz dw79.av2xp . gbmy gc s6pi pra4fo9fwq k   j-ppy -3vpf   o k4hy3 -!..5s ,2 k5 j p38dtd   !i   b!fgj,nx qgif ")
    for s in ss:
        result = solu.countValidWords(s)
    
        output_Str = ' result = ' + str(result)
        print(output_Str)