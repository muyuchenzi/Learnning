# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self, list_var1=[3, 4, 6], list_var2=[4, 7, 4]):
        self.list_var1 = list_var1
        self.list_var2 = list_var2

    def listToNode(self, list_var: list):
        list_head, *list_tail = list_var
        list_node_tail = ListNode(list_head)
        while list_var:
            list_node_tail.next = ListNode(list_var.pop())
            print(list_node_tail.next)
        return list_node_tail

    def convert(self):
        ListNode_var1 = self.listToNode(list_var=self.list_var1)
        ListNode_var2 = self.listToNode(list_var=self.list_var2)
        return ListNode_var1, ListNode_var2

    def addTwoNumbers(self):
        carry = 0  # 记录进位
        while self.list_var1 or self.list_var2 or carry:
            pass


if __name__ == '__main__':
    answer = Solution()
    l1, l2 = answer.convert()

