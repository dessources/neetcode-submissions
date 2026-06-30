# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
    
        if head and head.next:
            s = head
            f = head.next.next

            while s and f and f.next:
                if s.val == f.val:
                    return True
                s = s.next
                f = f.next.next
        return False