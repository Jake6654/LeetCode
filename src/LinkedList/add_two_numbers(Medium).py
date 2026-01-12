
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Create new LinkedList with a dummy node to keep track the sum of two node from l1 and l2
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        # keep iterating until all of those are None
        while l1 or l2 or carry:
            # Assign values to v1 and v2
            if l1 is not None:
                v1 = l1.val
            else:
                v1 = 0
            if l2 is not None:
                v2 = l2.val
            else:
                v2 = 0

            # Add up two vals
            sum = v1 + v2 + carry
            # Check Sum whether it has carry
            carry = sum // 10
            # the value I'm gonna put it to new LinkedList
            digit = sum % 10

            curr.next = ListNode(digit)
            curr = curr.next

            # Need to update l1 and l2
            if l1 is not None:
                l1 = l1.next
            else:
                l1 = None
            if l2 is not None:
                l2 = l2.next
            else:
                l2 = None

        return dummy.next


