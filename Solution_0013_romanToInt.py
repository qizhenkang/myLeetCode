import string
import math
from typing import List


class Solution:
    def romanToInt(self, s: str) -> int:
        library = {'I': 1, 'V': 5, 'X': 10,
                   'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        # sign = +1
        # library_pointer = 0
        temp = 0
        for i in range(len(s)):
            if i > 0:
                temp = int(library[s[i]] / library[s[i - 1]])

            if temp == 5 or temp == 10:
                result = result + library[s[i]] - 2 * library[s[i - 1]]
            else:
                result = result + library[s[i]]

        return result


if __name__ == '__main__':
    solu = Solution()

    input_Str = str('IX')
    input_List = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    input_int = 101

    # output_Str = 'result = ' + solu.intToRoman(input_int)
    output_Str = 'result = ' + str(solu.romanToInt(input_Str))
    print(output_Str)
