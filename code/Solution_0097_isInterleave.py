# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 19:51:47 2021

@author: qizhe
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        读题：
        1、难点在于不知道字母来自于哪里，所以需要回溯
        
        测试：
        1、超时了，这是我没想到的，感觉已经是效率很高了，没办法呢
        
        答案：
        1、看了答案是动态规划，
        2、有人做了DFS“记忆化搜索”，那么存在的问题，其实是，合理剪枝
        
        测试：
        1、想办法剪枝，看到现象是，有些情况确实进行了多次比较
        2、测试通过，性能很好
        
        总结：
        1、这个题让我学会了“记忆化搜索”
        2、记忆化搜索 是在一个  二叉树   中寻找正确搜索路径
        3、动态规划  是在一个  二维数组  中寻找正确搜索路径
        """
        
        def __dfs(s1,s2,s3,s1pointer,s2pointer,s3pointer,memo):
            # print(s1pointer,s2pointer,s3pointer)
            if s3pointer >= len(s3) and s1pointer == len(s1) and s2pointer == len(s2) :
                return True
        
            # if s3pointer >= len(s3) or s1pointer == len(s1) or s2pointer == len(s2) :
            print(s1pointer,s2pointer,s3pointer)
            if s1pointer == len(s1):
                # print()
                if s3[s3pointer:] != s2[s2pointer:]:
                    return False
                else:
                    return True
            
            if s2pointer == len(s2):
                if s3[s3pointer:] != s1[s1pointer:]:
                    return False
                else:
                    return True
                
            if (s1pointer,s2pointer) in memo:
                return False
            
            result = False
            if s1pointer < len(s1) and s3[s3pointer] == s1[s1pointer]:
                result |= __dfs(s1,s2,s3,s1pointer+1,s2pointer,s3pointer+1,memo)
                
            if not result and s2pointer < len(s2) and s3[s3pointer] == s2[s2pointer]:
                result |= __dfs(s1,s2,s3,s1pointer,s2pointer+1,s3pointer+1,memo)
            
            if not result:
                memo.add((s1pointer,s2pointer))
            
            return result
        
        if len(s1) + len(s2) != len(s3):
            return False

        memo = set()
        result = __dfs(s1,s2,s3,0,0,0,memo)
        print(memo)
        return result
        
        # return memo

if __name__ == '__main__':
    solu = Solution()

    input_Str = str('hello')
    # input_List = []
    # input_List = TreeNode(1)
    # input_List.left = TreeNode(2)
    # input_List.right = TreeNode(3)
    # s1 = 'aa'
    # s2 = 'ab'
    # s3 = 'aaba'
    s1 = "aabcc"
    s2 = "dbbca"
    # s3 = "aadbbcbcac"
    s3 = "aadbbbaccc"
    # s1 = "cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc"
    # s2 = "abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb"
    # s3 = "abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb"
   
    result = solu.isInterleave(s1,s2,s3)

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = ' result = ' + str(result)
    print(output_Str)