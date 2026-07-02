# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        carry = 0
        
        while l1 and l2:
            cur_sum = l1.val + l2.val + carry
            cur.next = ListNode(cur_sum % 10)
            carry = cur_sum // 10
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
            
        while l1:
            cur_sum = l1.val + carry
            cur.next = ListNode(cur_sum % 10)
            carry = cur_sum // 10
            l1 = l1.next
            cur = cur.next
            
        while l2:
            cur_sum = l2.val + carry
            cur.next = ListNode(cur_sum % 10)
            carry = cur_sum // 10
            l2 = l2.next
            cur = cur.next
        
        if carry:
            cur.next = ListNode(1)
        
        return head.next