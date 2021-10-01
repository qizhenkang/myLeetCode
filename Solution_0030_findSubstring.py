# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 10:51:59 2021

@author: qizhe
"""

class Solution:
    def findSubstring(self, s: str, words):
        """
        这个题有几个特点：
        1、给了一个字符串，给了一个words表，让你找
        2、words里面的词长度都一样，且不区分顺序
        3、让你找所有words拼成的字符串，不考虑顺序
        
        感觉用哈希表+栈可以
        """
        result = []
        wordDict = {}
        for i,word in enumerate(words):
            if word not in wordDict:
                wordDict[word] = 1
            else:
                wordDict[word] += 1
        
        # ……一个是单词长度，一个是词汇表长度
        wordlength = len(words[0])
        wordslength = len(words)
        for k in range(wordlength):
            i = wordlength + k
            wordstack = []
            numstack = []
            while i <= len(s):
            # for i in range(wordlength,len(s)):
                
                word = s[i-wordlength:i]
                if word in wordDict:
                    # 清空栈中无关元素
                    # while wordDict[word] in wordstack:
                    #     wordstack.pop(0)
                    #     numstack.pop(0)
                    # 实际上是一个队列
                    if len(wordstack) == wordslength:
                        wordstack.pop(0)
                        numstack.pop(0)
                    wordstack.append(word)
                    numstack.append(i-wordlength)
                else:
                    wordstack = []
                    numstack = []
                i += wordlength
                
                # 计算当前队列内的词频是否满足要求
                if len(numstack) == wordslength:
                    stackDict = {}
                    for word in wordstack:
                        if word not in stackDict:
                            stackDict[word] = 1
                        else:
                            stackDict[word] += 1
                    
                    AimFlag = 1
                    for word in stackDict:
                        if word in wordDict:
                            if stackDict[word] != wordDict[word]:
                                AimFlag = 0
                        else:
                            AimFlag = 0
                    if AimFlag:
                        if numstack[0] not in result:
                            result.append(numstack[0])
                
            # if len(numstack) == wordslength:
            #     result.append(numstack[0])
            
            # print('wordstack ',wordstack)
            # print('numstack  ',numstack)

        return result
        


if __name__ == '__main__':
    solu = Solution()
    # input_List = [4,5,6,7,0,1,2]
    # input_aim = 0
    # n5 = ListNode(5)
    # n4 = ListNode(4,n5)
    # n3 = ListNode(3,n4)
    # n2 = ListNode(2,n3)
    # n1 = ListNode(1,n2)
    s = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]
    # s = "wordgoodgoodgoodbestword"
    # words = ["word","good","best","word"]
    # s = "barfoothefoobarman"
    # words = ["foo","bar"]
    s = "foobarfoobarthefoobarman"
    words = ["foo","bar"]
    
    # s = "wordgoodgoodgoodbestword"
    # words = ["word","good","best","good"]
    # s = "aaaaaaaaaaaaaa"
    # words = ["aa","aa"]
    # s = "mississippi"
    # words = ["si","is"]

    # result = solu.swapPairs(n1)
    result = solu.findSubstring(s,words)
    
    # print('result = ',end ='')
    # while result:
    #     print(result.val, end=" ")
    #     result = result.next
    output_Str = 'result = ' + str(result)
    print(output_Str)
