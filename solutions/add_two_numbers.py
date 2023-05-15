# Runtime 83 ms Beats 16.99%
# Memory 16.3 MB Beats 17.11%

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = self.list_to_number(l1)
        n2 = self.list_to_number(l2)

        total = n1 + n2

        return self.number_to_list(total)

    def list_to_number(self, head: ListNode) -> int:
        number = 0
        multiplier = 1
        current = head

        while current is not None:
            number += current.val * multiplier
            multiplier *= 10
            current = current.next

        return number

    def number_to_list(self, number: int) -> Optional[ListNode]:
        if number == 0:
            return ListNode(0)

        head = None
        current = None

        while number > 0:
            digit = number % 10
            number //= 10
            node = ListNode(digit)

            if head is None:
                head = node
                current = node
            else:
                current.next = node
                current = node

        return head
