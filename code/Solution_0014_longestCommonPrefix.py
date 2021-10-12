import string
import math
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        if len(strs) > 0:
            result = strs[0]
            for str_i in strs[1:]:  # todo 从第2元素开始
                for j in range(len(result)):
                    if j < len(str_i):
                        if result[j] != str_i[j]:
                            result = result[:j]
                            break
                    else:
                        result = result[:j]
                        break

        return result


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('IX')
    input_List = ['a', 'dsa']
    input_int = 101

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + solu.longestCommonPrefix(input_List)
    print(output_Str)
