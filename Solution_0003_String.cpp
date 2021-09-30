class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        int result = 0;
        int Length = s.length(), aim_length; // ? 获取长度
        int i, j;
        char s_i;
        string aim;
        for (i = 0; i < Length; i++)
        {
            s_i = s[i];
            aim_length = aim.length();
            for (j = 0; j < aim_length; j++)
            {
                if (s_i == aim[j])
                {
                    break;
                }
                if (j == aim_length - 1) // ! 到最后一个了，依然没有相等，即可以添加了
                {
                    aim.push_back(s_i); // 把当前的加入
                    result++;
                }
            }
            if (aim_length == 0)
            {
                aim[0] = s_i;
                aim_length = 1;
            }
            result = result > aim_length ? result : aim_length;
        }

        return result;
    }
};