# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode],  k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self.getKthNode(group_prev, k)
            if not kth:
                break
            
            group_next = kth.next
            
            prev, cur = group_next, group_prev.next
            while cur != group_next:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
                
        return dummy.next

    def getKthNode(self, curr: Optional[ListNode], k:  int) -> Optional[ListNode]:
        # Helper specifically designed to walk k steps  and return the node
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr