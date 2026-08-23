# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node_list = list()
        node = head

        while node:
            node_list.append(node)
            node = node.next
        
        left = 0
        right = len(node_list) - 1

        while left < right:
            node_list[left].next = node_list[right]
            left += 1
            node_list[right].next = node_list[left]
            right -= 1
        node_list[left].next = None
        