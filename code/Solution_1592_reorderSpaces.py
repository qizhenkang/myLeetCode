# -*- coding: utf-8 -*-
"""
Created on 2022/09/07 19:07:30

@author: Qi Zhenkang, Tsinghua Univ.

Copyright © 2022. All rights reserved.
"""


class Solution:
    def reorderSpaces(self, text: str) -> str:
        """
        reorderSpaces _summary_

        需要统计单词数，单位起始位置，空格数，以及计算空格平分个数，最后放在最后

        1. 统计单词数及开始位置、以及空格数
        2. 开辟新字符串，放单词、放空格
        3. 结尾放剩余空格

        用时 15 min 1 次提交

        写完后以为可以一次通过的，结果debug了几个错误

        Args:
            text (str): _description_

        Returns:
            str: _description_
        """

        space_flag = True
        word_list = []
        _start = 0
        _end = 0
        space_num = 0
        for i, s in enumerate(text):
            if s == ' ':
                if not space_flag:
                    _end = i
                    word_list.append(text[_start:_end])
                space_num += 1
                space_flag = True
            else:
                if space_flag:
                    _start = i
                space_flag = False

        if not space_flag:  # 非空格结尾
            _end = len(text)
            word_list.append(text[_start:_end])

        word_space_num = int(len(word_list)-1)

        if word_space_num == 0:
            result = word_list[0] + ' '*space_num
            return result

        space_per = space_num // word_space_num
        space_end = space_num - space_per * word_space_num

        # print(space_num, word_space_num, space_end)

        result = word_list[0]
        for word in word_list[1:]:
            result += ' '*space_per
            result += word

        result += ' '*space_end

        return result


if __name__ == '__main__':
    solu = Solution()

    # "this   is   a   sentence"
    print(solu.reorderSpaces('  this   is  a sentence '))
    # "practice   makes   perfect "
    print(solu.reorderSpaces(' practice   makes   perfect'))
    print(solu.reorderSpaces('hello   world'))  # "hello   world"
    # "walks  udp  package  into  bar  a "
    print(solu.reorderSpaces('  walks  udp package   into  bar a'))
    print(solu.reorderSpaces('a'))  # "a"
