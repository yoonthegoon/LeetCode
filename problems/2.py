# https://leetcode.com/problems/add-two-numbers/


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    @staticmethod
    def node_to_int(list_node: ListNode) -> int:
        str_node = ""
        while True:
            str_node += str(list_node.val)
            list_node = list_node.next
            if not list_node:
                break
        return int(str_node[::-1])

    @staticmethod
    def int_to_node(output: int) -> ListNode:
        str_node = str(output)[::-1]
        list_node = ListNode(int(str_node[-1]))
        str_node = str_node[:-1]
        while str_node:
            list_node = ListNode(int(str_node[-1]), list_node)
            str_node = str_node[:-1]
        return list_node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.int_to_node(self.node_to_int(l1) + self.node_to_int(l2))
