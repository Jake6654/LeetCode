# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head.next == None:
            return False
        seen = set()
        current = head


        # When we revisit the same node, that means there's a cycle
        # Need to keep track of the visited node
        while current:
            if current not in seen:
                seen.add(current)
                current = current.next
            else:
                return True
        return False



