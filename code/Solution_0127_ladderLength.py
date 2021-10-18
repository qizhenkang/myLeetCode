# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:48:12 2021

@author: qizhe
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        """
        读题：
        1、周赛考到了一个BFS，故意找了一个BFS的题目来做，找最短路径，应该就是典型的BFS题吧
        2、但这个感觉不那么简单，需要处理一下各个单词，获得词向量
        3、如何最快地找到最短路径？应该是每一步都是在这一步计算完成后进行，找当前的最小步数的
        
        测试：
        1、通不过，找到的不是最小的，算法好像是一个贪婪算法，很可能不是全局最小。
        
        不会做看答案
        
        答案：
        1、和答案的思路是一致的，答案的意思要：BFS + 建图
        2、建图我还不太懂，BFS 我也不太懂，这题做出来就见鬼了
        3、这题的内核是找最短路径，与周赛263最后一题极其相似，搞懂应该就可以做出周赛题了
        """
        
        def bfs(wordList,wordScoreList,currentWord,endWord,depth,wordLength,wordListLength,used):
            print(currentWord,depth,wordListLength)
            if currentWord == endWord:
                # print(currentWord,depth)
                return depth+1
            if depth > wordListLength:
                return 0
            
            # for v in range(wordLength):
            #     if currentWord[v] != endWord[v]:
            #         # 这里不好弄，是决策的关键
            #         # 这里用贪婪，找相似度最大的？
                    
            scoreNow = 0
            scoreMax = -1
            nextWordNum = -1
            for n in range(len(wordList)):
                if wordList[n] == currentWord:
                    used[n] = True
                if used[n]:
                    continue
                scoreNow = 0
                for i in range(wordLength):
                    if currentWord[i] == wordList[n][i]:
                        scoreNow += 1
                if scoreNow >= wordLength-1:
                    if wordScoreList[n] > scoreMax:
                        scoreMax = wordScoreList[n]
                        nextWordNum = n
            result = 0
            if nextWordNum > -1:
                used[nextWordNum] = True
                result = bfs(wordList,wordScoreList,wordList[nextWordNum],endWord,depth+1,wordLength,wordListLength,used)
                used[nextWordNum] = False
                        
                    
                    # currentWord[v] = 1
                    # if currentWord in wordList:
                    #     bfs(wordList,currentWord,endWord,depth+1,length)
                    # currentWord[v] = 0
            
            return result
        
        wordLength = len(endWord)
        wordListLength = len(wordList)
        # beginWordVector = [0]*N
        # endWordVector = [0]*N
        # for i in range(N):
        #     beginWordVector[i] = ord(beginWord[i])
        #     endWordVector[i] = ord(endWord[i])
        wordScoreList = [0]*wordListLength
        for n in range(wordListLength):
            for i in range(wordLength):
                if wordList[n][i] == endWord[i]:
                    wordScoreList[n] += 1
        # print(wordScoreList)
            
        
        # wordVectorList = []
        # for word in wordList:
        #     wordVector = [0]*N
        #     for i in range(N):
        #         wordVector[i] = ord(word[i])
        #     wordVectorList.append(wordVector)
        # print(wordVectorList,beginWordVector,endWordVector)
        if wordLength not in wordScoreList:
            return 0
        # 词向量已知之后，就可以搜索了吧？
        
        # print(beginWordVector)
        used = [False] * wordListLength
        
        
        return bfs(wordList,wordScoreList,beginWord,endWord,0,wordLength,wordListLength,used)
    
if __name__ == '__main__':
    solu = Solution()

    # nums = [3,2,1,5]
    n = 8
    # edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
    # time = 3
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","cot",'cog']
    wordList = ["hot","dot","dog","lot","log"]
    beginWord = "ymain"
    endWord = "oecij"
    wordList = ["ymann","yycrj","oecij","ymcnj","yzcrj","yycij","xecij","yecij","ymanj","yzcnj","ymain"]
    result = solu.ladderLength(beginWord,endWord,wordList)

    output_Str = ' result = ' + str(result)
    print(output_Str)