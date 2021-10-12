

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        result = str()
        if numRows == 1:
            result = s
        else:
            list_result = [''] * numRows
            row = 0
            direction = -1  # !初始为-1 是为了符合逻辑
            for i in range(len(s)):
                list_result[row] = list_result[row] + s[i]
                if row == numRows - 1 or row == 0:  # ! 到边界时换向
                    direction = -direction
                row = row + direction

            for k in range(numRows):
                result = result + list_result[k]

        return result


if __name__ == '__main__':
    solu = Solution()
    input_numRows = 2
    input_Str = str('LEETCODEISHIRING')
    output_Str = 'result = ' + solu.convert(input_Str, input_numRows)
    print(output_Str)
