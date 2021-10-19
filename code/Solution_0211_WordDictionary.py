# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 09:16:04 2021

@author: qizhe
"""

class WordDictionary:
    """
    读题
    1、这个题的难点在于，应该采用一个什么数据结构，来使得'.'造成的影响最小
    2、以及如何处理'.'的情况，难道要一个一个试吗
    
    测试：
    1、错了两次，通过了，性能不太好
    
    答案：
    1、用了所谓的“字典树”数据结构，与我的分析是一致的，也就是要用一种合适的数据结构来完成任务
    """

    def __init__(self):
        self.wordDict = []
        # self.maxLength = 0
        self.length = []
        
        return


    def addWord(self, word: str) -> None:
        if word not in self.wordDict:
            self.wordDict.append(word)
            self.length.append(len(word))
            # self.maxLength = max(self.maxLength,len(word))
        return


    def search(self, word: str) -> bool:
        """
        有两种情况
        1、一种情况是wordDict很大，word的'.'不多，要找很麻烦
        2、wrodDict很小，word含很多'.'很麻烦
        """
        
        if word in self.wordDict:
            return True
        wordLength = len(word)
        if wordLength not in self.length:
            return False
    
        wordListLength = len(self.wordDict)
        wordSearch = [True] * wordListLength
        falseCnt = 0
        result = True
        # 先按照最朴素的思想来找
        for i in range(wordLength):
            falseCnt = 0
            if word[i] != '.':
                for j in range(wordListLength):
                    print(i,j,falseCnt)
                    if not wordSearch[j]:
                        falseCnt += 1
                        continue
                    if len(self.wordDict[j]) != wordLength or word[i] != self.wordDict[j][i]:
                        wordSearch[j] = False
                        falseCnt += 1
            if falseCnt == wordListLength:
                # print('falseCnt == wordListLength')
                result = False
                break
        return result
if __name__ == '__main__':
    # solu = Solution()

    # nums = [3,2,1,5]
    # n = 5
    # edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
    # time = 3
    # change = 5
    
    # Your WordDictionary object will be instantiated and called as such:
    obj = WordDictionary()
    obj.addWord('ba')
    obj.addWord('baea')
    obj.addWord('baaax')
    obj.addWord('baf')
    param_2 = obj.search('.')
    print(param_2)
    # n = 11
    # edges = [[1,2],[1,3],[1,4],[2,5],[5,6],[3,7],[4,8],[4,9],[9,10],[10,11]]
    # time = 8
    # change = 584
    # n = 6
    # edges = [[1,2],[2,3],[2,4],[2,5],[5,6],[4,1],[5,3]]
    # time = 457
    # change = 953
    # n = 19
    # edges = [[1,2],[2,3],[1,4],[2,5],[2,6],[2,7],[7,8],[8,9],[7,10],[9,11],[11,12],[1,13],[3,14],[13,15],[14,16],[8,17],[4,18],[11,19],[17,11],[3,19],[19,7],[12,5],[8,1],[15,7],[19,6],[18,9],[6,8],[14,19],[13,18],[15,2],[13,12],[1,5],[16,18],[3,16],[6,1],[18,14],[12,1],[16,6],[13,11],[1,14],[16,13],[11,16],[4,15],[17,5],[5,9],[12,2],[4,10],[9,16],[17,9],[3,5],[10,2],[18,1],[15,18],[12,17],[10,6],[10,18],[19,12],[12,15],[19,13],[1,19],[9,14],[4,3],[17,13],[9,3],[17,10],[19,10],[5,4],[5,7],[14,17],[1,10],[4,11],[6,4],[5,10],[7,14],[8,14],[18,17],[15,10],[11,8],[14,11],[7,3],[5,18],[13,8],[4,12],[11,3],[5,15],[15,9],[8,10],[13,3],[17,1],[10,11],[15,11],[19,2],[1,3],[7,4],[18,11],[2,14],[9,1],[17,15],[7,13],[12,16],[12,8],[6,12],[9,6],[2,17],[15,6],[16,2],[12,7],[7,9],[8,4]]
    # time = 850
    # change = 411
    # result = solu.secondMinimum(n, edges, time, change)

    # output_Str = ' result = ' + str(result)
    # print(output_Str)

