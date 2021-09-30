import string
import math
from typing import List


class Solution:
    def intToRoman(self, num: int) -> str:
        result = str()
        current_str = str()
        library = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        temp_num = num
        i = 0
        rank = 0  # ?判断当前所在位
        library_pointer = 0
        while temp_num != 0:
            i = temp_num % 10  # todo 取位
            library_pointer = rank * 2   # ! 指向1 / 10 / 100

            if i == 9:
                current_str = library[library_pointer] + \
                    library[library_pointer + 2]
            elif i == 8:
                current_str = library[library_pointer +
                                      1] + library[library_pointer] * 3
            elif i == 7:
                current_str = library[library_pointer +
                                      1] + library[library_pointer] * 2
            elif i == 6:
                current_str = library[library_pointer +
                                      1] + library[library_pointer] * 1
            elif i == 5:
                current_str = library[library_pointer + 1]
            elif i == 4:
                current_str = library[library_pointer] + \
                    library[library_pointer+1]
            elif i == 3:
                current_str = library[library_pointer] * 3
            elif i == 2:
                current_str = library[library_pointer] * 2
            elif i == 1:
                current_str = library[library_pointer] * 1
            elif i == 0:
                current_str = ''
            result = current_str + result

            temp_num = int(temp_num / 10)
            rank = rank + 1

        return result


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('    -42  3sd')
    input_List = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    input_int = 101

    output_Str = 'result = ' + solu.intToRoman(input_int)
    print(output_Str)
