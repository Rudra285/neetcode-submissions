# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2

        sorted_list_node = sorted_list = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                sorted_list_node.val = list1.val
                list1 = list1.next
            else:
                sorted_list_node.val = list2.val
                list2 = list2.next
            sorted_list_node.next = ListNode()
            sorted_list_node = sorted_list_node.next
        
        while list1:
            sorted_list_node.val = list1.val
            list1 = list1.next
            if list1:
                sorted_list_node.next = ListNode()
                sorted_list_node = sorted_list_node.next

        while list2:
            sorted_list_node.val = list2.val
            list2 = list2.next
            if list2:
                sorted_list_node.next = ListNode()
                sorted_list_node = sorted_list_node.next
            
        return sorted_list