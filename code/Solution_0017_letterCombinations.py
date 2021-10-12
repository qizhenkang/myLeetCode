import string
import math
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        9月30回溯算法，重写
        """
        def dfs(library,digits,num,current,result,length):
            if num == length:
                result.append(current)
                return
            for i in library[digits[num]]:
                dfs(library, digits, num+1, current + i, result, length)
            
            return
        
        library = {'2': 'abc',
                   '3': 'def',
                   '4': 'ghi',
                   '5': 'jkl',
                   '6': 'mno',
                   '7': 'pqrs',
                   '8': 'tuv',
                   '9': 'wxyz'}
        N = len(digits)
        if not N:
            return []
        current = ''
        result = []
        dfs(library,digits,0,current,result,N)
        return result

        # d_Length = len(digits)  # 数据长度
        # pointers = [0] * d_Length  # 指针组
        # pointers_end = [0] * d_Length

        # count_All = 1
        # temp = 0
        # p = 0
        # for i in digits:  # todo 确定result的长度 更新指针组的数据
        #     temp = len(library[i])
        #     count_All *= temp
        #     pointers_end[p] = temp
        #     p += 1

        # count = 0
        # result = []
        # breakflag = 1
        # while breakflag:
        #     if digits == '':
        #         result = []
        #         break
        #     current_str = str()
        #     for i in range(d_Length):
        #         current_str += library[digits[i]][pointers[i]]
        #     result.append(current_str)
        #     # print(str(pointers))

        #     pointers[-1] += 1

        #     for i in range(d_Length - 1, -1, -1):
        #         if pointers[i] == pointers_end[i]:
        #             if i == 0:
        #                 breakflag = 0  # 此处是结束标志
        #             else:
        #                 pointers[i - 1] += 1
        #                 pointers[i] = 0
        #         else:
        #             break
        #     count += 1

        # return result


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('23')
    input_List = [-55, -24, -18, -11, -7, -3, 4, 5, 6, 9, 11, 23, 33]
    input_int = 0

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(solu.letterCombinations(input_Str))
    print(output_Str)
