# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        curr = dummy

        # need to iterate all elements in Arrays once, list1 and list2
        # time complexity: O(n+m)
        # use a dummy node and two pointers to merge the lists by appending
        # the smaller current node when iterating
        while list1 is not None and list2 is not None:
            if list1.val >= list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next

        # if one of the lists is done
        # then just attach remaining node
        if list1 is not None:
            curr.next = list1
        else:
            curr.next = list2

        return dummy.next




