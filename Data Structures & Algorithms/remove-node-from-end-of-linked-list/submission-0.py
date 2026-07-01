# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head:
            count =1
            s, f = head, head.next
            
            while f and f.next:
                f = f.next.next
                count+=2
            if f:
                count+=1
         
            i=0 
            prev = None 
            while count-i > n:
                prev = s
                s=s.next
                i+=1
            if prev:
                prev.next = s.next
                return head
            else: return s.next
        return None