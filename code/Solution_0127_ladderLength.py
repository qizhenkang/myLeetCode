# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:48:12 2021

@author: qizhe
"""
from typing import List
from collections import defaultdict, deque
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
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
        
        def __bfs(wordSet,beginWord,endWord,wordLength):
            """
            BFS建图，核心是建立按层建立图
            """
            depth = 0
            found = False
            
            # 建立层次队列
            queue = deque()
            queue.append(beginWord)
            
            # 建立访问集，防止多次访问/成环
            nextWordVisited = set()
            Visited = set()
            Visited.add(beginWord)
            while queue:
                depth += 1
                # 这里是因为队列是动态的，所以要保存最开始的长度
                queueLength = len(queue)
                for i in range(queueLength):
                    currentWord = queue.popleft()
                    # originalWord = currentWord
                    currentWordList = list(currentWord)
                    for j in range(wordLength):
                        originalChar = currentWordList[j]
                        for k in string.ascii_lowercase:
                            currentWordList[j] = k
                            newWord = "".join(currentWordList)
                            # print(newWord)
                            # 防止重复
                            if newWord not in Visited:
                                # 判断字典表里是否存在这个词
                                if newWord in wordSet:
                                    if newWord == endWord:
                                        found = True
                                    
                                    if newWord not in nextWordVisited:
                                        nextWordVisited.add(newWord)
                                        queue.append(newWord)

                        currentWordList[j] = originalChar
                # 是不是这里提前结束，可以保证建的图是最短的？
                if found:
                    break
                Visited |=  nextWordVisited
                nextWordVisited = set()

            return depth+1 if found else 0

        wordSet = set(wordList)
        if not wordSet or endWord not in wordSet:
            return 0
        
        wordLength = len(endWord)
        
        return __bfs(wordSet,beginWord,endWord,wordLength)
    
if __name__ == '__main__':
    solu = Solution()

    # nums = [3,2,1,5]
    n = 8
    # edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
    # time = 3
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","cot",'cog']
    wordList = ["hot","dot","dog","lot","log","cog"]
    beginWord = "ymain"
    endWord = "oecij"
    wordList = ["ymann","yycrj","oecij","ymcnj","yzcrj","yycij","xecij","yecij","ymanj","yzcnj","ymain"]
    result = solu.ladderLength(beginWord,endWord,wordList)

    output_Str = ' result = ' + str(result)
    print(output_Str)