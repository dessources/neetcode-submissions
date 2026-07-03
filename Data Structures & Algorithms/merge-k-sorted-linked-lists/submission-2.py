# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode])  -> Optional[ListNode]:
        head = ListNode()
        cur = head
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = ListNode(l1.val)
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                cur = cur.next
                l2  = l2.next
        
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
            
        return head.next
            
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n:
            while n > 1:
                for i in range(n//2):
                    lists[i] = self.mergeTwoLists(lists[2*i], lists[2*i +1])
                if n%2:
                    lists[n//2] = lists[n-1]
                    n=n+1
                n = n //2
            
            return lists[0]
        return None