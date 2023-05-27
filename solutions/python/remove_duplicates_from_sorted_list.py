# Runtime 57 ms Beats 12.90%
# Memory 16.4 MB Beats 7.54%

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
            
            if not head:
                return head
    
            current = head
    
            while current.next:
                if current.val == current.next.val:
                    current.next = current.next.next
                else:
                    current = current.next
    
            return head