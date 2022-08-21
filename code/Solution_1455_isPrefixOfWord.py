# -*- coding: utf-8 -*-
"""
Created on 2022/08/21 11:47:31

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        """
        isPrefixOfWord _summary_

        7 min 一次通过 模拟了一下而已 不太把握提交的

        其实写的有点乱，逻辑不清楚的。

        本质上再考双指针 问题不大。

        Args:
            sentence (str): _description_
            searchWord (str): _description_

        Returns:
            int: _description_
        """

        current_position = 1
        word_flag = True
        result = -1
        for i, s in enumerate(sentence):
            # 外层循环找开头
            if s == ' ':
                current_position += 1
                word_flag = True
                continue
            if word_flag:
                # 内层循环判匹配
                cnt = 0
                for j, w in enumerate(searchWord):
                    if sentence[i+cnt] != w:
                        break

                    cnt += 1
                else:
                    result = current_position
                    break

                word_flag = False

        return result


if __name__ == '__main__':
    solu = Solution()

    sentence = "i love eating burger"
    searchWord = "burg"

    print(solu.isPrefixOfWord(sentence, searchWord))

    sentence = "this problem is an easy problem"
    searchWord = "pro"

    print(solu.isPrefixOfWord(sentence, searchWord))

    sentence = "i am tired"
    searchWord = "you"

    print(solu.isPrefixOfWord(sentence, searchWord))
