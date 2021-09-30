/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * ? sd
 * todo
 * };
 */
class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        ListNode result1, result2, listx;
        int i = 0, x = 0, y = 0, z = 0;
        ListNode *result;
        ListNode *temp, *NewNode;

        // todo 0 新建头元素
        temp = new ListNode(0, nullptr);
        result = temp;
        while (l1 != nullptr || l2 != nullptr)
        {
            // todo 1 新建元素
            NewNode = new ListNode(0, nullptr);

            // todo 2 计算当前元素数字 特殊判断两者不同长度
            if (l1 != nullptr && l2 != nullptr)
            {
                x = l1->val + l2->val;
            }
            else if (l1 == nullptr)
            {
                x = l2->val;
            }
            else
            {
                x = l1->val;
            }
            z = x + y;
            NewNode->val = z % 10;
            y = (z >= 10) ? 1 : 0; // ? 保留进位符

            // todo 3 更新前一元素指针
            temp->next = NewNode;

            // todo 4 指针更新
            temp = NewNode;

            // todo 迭代读取新的元素
            if (l1 != nullptr) // ? 这里已经没问题了
            {
                l1 = l1->next;
            }
            if (l2 != nullptr)
            {
                l2 = l2->next;
            }
        }
        if (y != 0)
        {
            temp->next = new ListNode(y, nullptr);
        }
        return result->next;
    }
};