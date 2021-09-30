

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        # temp = 0
        sign = 1 if x >= 0 else -1
        digit = abs(x)
        while digit != 0:
            result = result * 10 + digit % 10
            digit = int(digit / 10)
        result = sign * result
        if (result > 2 ** 31 - 1 or result < -2 ** 31):
            result = 0

        return result


if __name__ == '__main__':
    solu = Solution()
    # input_numRows = 2
    # input_Str = str('LEETCODEISHIRING')
    input_num = 11223
    output_Str = 'result = ' + str(solu.reverse(input_num))
    print(output_Str)
