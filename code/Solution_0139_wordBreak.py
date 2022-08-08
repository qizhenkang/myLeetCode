# -*- coding: utf-8 -*-
"""
Created on 2022/07/23 10:59:23

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        wordBreak _summary_

        感觉像是一个搜索，深度优先搜索

        用例过不去，搞了一个记忆化

        Args:
            s (str): _description_
            wordDict (List[str]): _description_

        Returns:
            bool: _description_
        """

        length = len(s)

        # 需要记忆状态

        memo = []

        def dfs(start, end) -> bool:
            # print(start, end, s[start:end])
            result = False

            if start >= length:
                return True

            if end > length:
                return False

            # print(start, end, s[start:end])

            for i in range(end, length+1):
                # print('for: %s' % (s[start:i]))
                if i not in memo and i - start <= 20 and s[start:i] in wordDict:
                    result = dfs(i, i+1)
                    if result:
                        break
                    else:
                        memo.append(i)
                        # print(memo)

            return result

        result = dfs(0, 1)

        return result


if __name__ == '__main__':
    solu = Solution()

    results = [
        False,
        True,
        True,
        True,
        True,
        False
    ]

    ss = [
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
        "bccdbacdbdacddabbaaaadababadad",
        "a",
        "leetcode",
        "applepenapple",
        "catsandog",
    ]

    wordDicts = [
        ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa",
            "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"],
        ["cbc", "bcda", "adb", "ddca", "bad", "bbb", "dad", "dac", "ba", "aa", "bd", "abab", "bb", "dbda", "cb", "caccc", "d", "dd", "aadb", "cc", "b", "bcc", "bcd", "cd", "cbca", "bbd",
            "ddd", "dabb", "ab", "acd", "a", "bbcc", "cdcbd", "cada", "dbca", "ac", "abacd", "cba", "cdb", "dbac", "aada", "cdcda", "cdc", "dbc", "dbcb", "bdb", "ddbdd", "cadaa", "ddbc", "babb"],
        ["a"],
        ["leet", "code"],
        ["apple", "pen"],
        ["cats", "dog", "sand", "and", "cat"],
    ]

    for i in range(6):  # len(ss)
        s = ss[i]
        wordDict = wordDicts[i]
        result = solu.wordBreak(s, wordDict)
        print(result)
        assert result == results[i]
