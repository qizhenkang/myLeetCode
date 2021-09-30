import string
import math
from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:

        max_str = str(s[0])
        max_Num = 1
        temp_str = str()
        temp_Num = 0

        for i in range(0, len(s)):
            if (max_Num >= len(s) - i):
                # print('i = '+str(i) + '  max_Num = ' + str(max_Num))
                break

            for j in range(len(s) - 1, i, -1):  # ? 从后向前找，这样找到的才可能是最大的

                if s[i] == s[j]:  # ! 发现可能的回文字段
                    # print(str(i)+' '+str(j)+' '+str(s[i]))
                    Num = j - i + 1
                    if Num == 2 or Num == 3:
                        temp_str = s[i:j+1]
                        temp_Num = Num
                        if temp_Num > max_Num:
                            max_str = temp_str
                            max_Num = temp_Num
                    elif Num % 2 == 0:  # 偶数个回文

                        if s[i:int((i + j + 1) / 2)] == s[j:int((i + j + 1) / 2)-1:-1]:
                            temp_str = s[i:j+1]
                            temp_Num = Num
                            if temp_Num > max_Num:
                                max_str = temp_str
                                max_Num = temp_Num

                    else:  # 奇数个回文
                        if s[i:int((i + j) / 2)] == s[j:int((i + j) / 2):-1]:
                            temp_str = s[i:j+1]
                            temp_Num = Num
                            if temp_Num > max_Num:
                                max_str = temp_str
                                max_Num = temp_Num

        return max_str


if __name__ == '__main__':
    solu = Solution()
    # num1 = [1, 2, 3]
    # num2 = [2, 3, 4]
    # result_Str = str('dvdf')
    input_Str = str('abccba')
    output_Str = 'result = ' + solu.longestPalindrome(input_Str)
    print(output_Str)
