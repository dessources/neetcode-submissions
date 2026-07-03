# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head:
            count = 0
            f = head
            while f and f.next:
                f = f.next.next
                count += 2
            if f:
                count += 1

            groups = count // k
            dummy = ListNode(0, head)
            cur = dummy

            group_prev, group_head = cur, cur.next
            cur = cur.next

            for i in range(groups):
                prev = temp = None
                for j in range(k-1):
                    temp = cur.next
                    cur.next = prev
                    prev = cur
                    cur = temp

                temp = cur.next
                cur.next = prev
                group_head.next = temp
                group_prev.next = cur
                group_prev = group_head
                group_head = temp
                cur = temp
            return dummy.next
        return None