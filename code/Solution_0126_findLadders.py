# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:48:12 2021

@author: qizhe
"""
from collections import defaultdict, deque
from typing import List

import string


class Solution:
        

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        读题：
        1、周赛考到了一个BFS，故意找了一个BFS的题目来做，找最短路径，应该就是典型的BFS题吧
        2、如何最快地找到最短路径？应该是每一步都是在这一步计算完成后进行，找当前的最小步数的
        3、本质上，是利用广度优先搜索建图，然后利用回溯进行搜索
        
        测试：
        1、通不过，找到的不是最小的，算法好像是一个贪婪算法，很可能不是全局最小。
        
        不会做看答案
        
        答案：
        1、和答案的思路是一致的，答案的意思要：BFS + 建图
        2、建图我还不太懂，BFS 我也不太懂，这题做出来就见鬼了
        3、这题的内核是找最短路径，与周赛263最后一题极其相似，搞懂应该就可以做出周赛题了
        4、BFS+DFS
        """
        def __bfs(wordSet,graphDict,beginWord,endWord,wordLength):
            """
            BFS建图，核心是建立按层建立图
            """
            
            found = False
            queue = deque()
            queue.append(beginWord)
            nextWordVisited = set()
            Visited = set()
            Visited.add(beginWord)
            while queue:
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
                                    graphDict[currentWord].add(newWord)
                        currentWordList[j] = originalChar
                # 是不是这里提前结束，可以保证建的图是最短的？
                if found:
                    break
                Visited |=  nextWordVisited
                nextWordVisited = set()

            return found
        
        def __dfs(result,current,wordSet,graphDict,beginWord,endWord,wordLength):
            """
            现在是已经有图了，你只需要给我找到所有解就可以了
            """
            if current[-1] == endWord:
                result.append(current)
                return
            
            # if graphDict[current[-1]]
            
            for word in graphDict[current[-1]]:
                __dfs(result,current+[word],wordSet,graphDict,beginWord,endWord,wordLength)
                # print(word)
            
            return
        
        wordSet = set(wordList)
        if not wordSet or endWord not in wordSet:
            return []
        
        wordLength = len(endWord)
        graphDict = defaultdict(set)
        found = __bfs(wordSet,graphDict,beginWord,endWord,wordLength)
        # print(graphDict)
        if not found:
            return []
        result = []
        current = [beginWord]
        __dfs(result,current,wordSet,graphDict,beginWord,endWord,wordLength)
        
        
        return result
        


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
    beginWord = "a"
    endWord = "c"
    wordList = ["a","b","c"]
    # beginWord = "ymain"
    # endWord = "oecij"
    # wordList = ["ymann","yycrj","oecij","ymcnj","yzcrj","yycij","xecij","yecij","ymanj","yzcnj","ymain"]
    result = solu.findLadders(beginWord,endWord,wordList)

    output_Str = ' result = ' + str(result)
    print(output_Str)