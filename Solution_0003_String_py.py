import string


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        aim_str = str()
        index = 0
        s_length = len(s)
        aim_length = 0
        for s_i in s:
            # result = result + 1
            index = 0
            for aim_j in aim_str:

                if s_i == aim_j:
                    aim_str = aim_str[index + 1:aim_length] + s_i  # !说明遇到相同字符了，清零
                    break

                if aim_j == aim_str[aim_length-1]:
                    aim_str = aim_str + s_i

                index = index + 1

            if aim_length == 0:
                aim_str = aim_str + s_i
                aim_length = 1
            aim_length = len(aim_str)
            result = result if result > aim_length else aim_length

        return result


if __name__ == '__main__':
    solu = Solution()
    result_Str = str('dvdf')
    output_Str = 'result = ' + str(solu.lengthOfLongestSubstring(result_Str))
    print(output_Str)
