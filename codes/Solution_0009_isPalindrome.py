class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = False
        y = x
        x_p = 0
        if x >= 0:
            while y != 0:
                x_p = x_p * 10 + y % 10
                y = int(y / 10)
            if x == x_p:
                result = True
        return result


if __name__ == '__main__':
    solu = Solution()
    # input_numRows = 2
    input_Str = str('    -42  3sd')
    # input_num = 11223
    output_Str = 'result = ' + str(solu.isPalindrome(-10))
    print(output_Str)
