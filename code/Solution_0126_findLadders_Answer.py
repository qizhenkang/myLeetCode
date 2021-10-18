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
        # 先将 wordList 放到哈希表里，便于判断某个单词是否在 wordList 里
        word_set = set(wordList)
        res = []
        if len(word_set) == 0 or endWord not in word_set:
            return res

        successors = defaultdict(set)
        # 第 1 步：使用广度优先遍历得到后继结点列表 successors
        # key：字符串，value：广度优先遍历过程中 key 的后继结点列表

        found = self.__bfs(beginWord, endWord, word_set, successors)
        # 这里就获取了层次遍历的图，并且同层之间没有联系
        print(successors)
        if not found:
            return res
        # 第 2 步：基于后继结点列表 successors ，使用回溯算法得到所有最短路径列表
        path = [beginWord]
        self.__dfs(beginWord, endWord, successors, path, res)
        return res

    def __bfs(self, beginWord, endWord, word_set, successors):
        # 新建队列
        queue = deque()
        queue.append(beginWord)
        
        # 记录是否已经走过
        visited = set()
        visited.add(beginWord)
        
        found = False
        word_len = len(beginWord)
        next_level_visited = set()

        while queue:
            # 获取当前队列，使该层所有元素逐个出队
            current_size = len(queue)
            for i in range(current_size):
                # 队列出队
                current_word = queue.popleft()
                word_list = list(current_word)
                
                # 当前词的逐个遍历
                for j in range(word_len):
                    
                    origin_char = word_list[j]
                    
                    # 遍历所有小写字母
                    for k in string.ascii_lowercase:
                        word_list[j] = k
                        next_word = ''.join(word_list)
                        # 判断 第j位 换成 k 字符，是否在图中
                        if next_word in word_set:
                            # 若未访问，
                            if next_word not in visited:
                                # 若找到结束的元素了
                                if next_word == endWord:
                                    found = True

                                # 避免下层元素重复加入队列
                                if next_word not in next_level_visited:
                                    # 这里是把下层入队的操作，他怕同一个元素进去两次，就乱了
                                    next_level_visited.add(next_word)
                                    # 下层入队
                                    queue.append(next_word)
                                
                                # 图中增加该词
                                successors[current_word].add(next_word)
                                print(current_word,next_word)
                    # 把原词恢复
                    word_list[j] = origin_char
            # 如果找到最后一个词了，就直接退出
            if found:
                # print
                break
            # 取两集合全部的元素（并集，等价于将 next_level_visited 里的所有元素添加到 visited 里）
            visited |= next_level_visited
            # 下层清空
            next_level_visited.clear()
        return found

    def __dfs(self, beginWord, endWord, successors, path, res):
        if beginWord == endWord:
            res.append(path[:])
            return

        if beginWord not in successors:
            return

        successor_words = successors[beginWord]
        for next_word in successor_words:
            # 这里是经典的回溯算法
            path.append(next_word)
            self.__dfs(next_word, endWord, successors, path, res)
            path.pop()



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
    # beginWord = "ymain"
    # endWord = "oecij"
    # wordList = ["ymann","yycrj","oecij","ymcnj","yzcrj","yycij","xecij","yecij","ymanj","yzcnj","ymain"]
    result = solu.findLadders(beginWord,endWord,wordList)

    output_Str = ' result = ' + str(result)
    print(output_Str)