class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self, list_var=[1, 2, 3, 4]):
        self.list_var = list_var

    def convertToListNode(self):
        listnode_res = ListNode(None)

        while self.list_var:
            print(self.list_var)
            node = self.list_var.pop()
            print(node)
            listnode_res = ListNode(node)
            print(listnode_res.val)
            listnode_res.next = self.list_var
            print(listnode_res.next)
        return listnode_res


if __name__ == '__main__':
    res = Solution()
    sss = res.convertToListNode()
