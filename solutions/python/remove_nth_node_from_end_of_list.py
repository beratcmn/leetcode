# Runtime 33 ms Beats 78.79% of users with Python3
# Memory 16.50 MB Beats 48.13% of users with Python3


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for i in range(1, n + 2):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next
