# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 19:35:24 2021

@author: qizhe
"""
import functools
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        """
        读题：
        1、题目我读懂了，就是随意分，分了之后可以交换 也可以不交换
        2、如何转换成一个数学问题，这才是最关键的
        3、显然不可能暴力求解，必然要想想办法/规律
        4、能不能找潜在的分界线？感觉上是可以的
        5、题目给了s最大是30，是不是潜在的告诉你，这个很复杂，尝试空间换时间？
        6、感觉上是，这个s2可以换成数组，这个数组是相对有序的，交换次数是有限的 N-1次
        7、一旦交换，就会使数组出现一个极值，所以最多有N-1个极值
        8、感觉像一个二叉树呢
        
        不知道考的什么，看答案吧
        
        答案：
        1、动态规划，完全不懂啊，看不进去，我要冷静冷静
        2、也有记忆化搜索的方案，感觉代码不错，我来试试
        
        测试：
        1、测试出了一些问题，成功了
        2、用memo自己写缓存，时间和内存双90% 性能极好
        3、所以这个题，就是典型的“记忆化搜索”
        """
        # @functools.lru_cache(maxsize=None, typed=False)
        # N = len(s1)
        # strDict = { s1[i]:i  for i in range(N)}
        # s2num = [strDict[s] for s in s2]
        # @cache 
        # 这个技术怎么实现？
        def __dfs(s1,s2,memo):
            print(s1,s2)
            N = len(s1)
            if N != len(s2) or (s1,s2) in memo:
                return False
            
            if s1 == s2:
                return True
            # 提前剪枝一下
            if sorted(s1) != sorted(s2):
                return False
            for i in range(1,N):
                if __dfs(s1[i:],s2[i:],memo) and __dfs(s1[:i],s2[:i],memo) or \
                    __dfs(s1[i:],s2[:N-i],memo) and __dfs(s1[:i],s2[N-i:],memo):
                        return True
            memo.add((s1,s2))
            return False
        memo = set()

        return __dfs(s1,s2,memo)
        
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
    # inputList = [2, 2]
    # time = 3
    # beginWord = "ymain"
    # endWord = "oecij"
    # wordList = ["ymann","yycrj","oecij","ymcnj","yzcrj","yycij","xecij","yecij","ymanj","yzcnj","ymain"]
    # s1 = "great"
    # s2 = "rgeat"
    # s1 = "abcde"
    # s2 = "caebd"
    s1 = "abb"
    s2 = "bba"
    s1 = "abc"
    s2 = "bca"
    s1 = "eebaacbcbcadaaedceaaacadccd"
    s2 = "eadcaacabaddaceacbceaabeccd"
    result = solu.isScramble(s1,s2)

    output_Str = ' result = ' + str(result)
    print(output_Str)