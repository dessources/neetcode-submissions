# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head:
            s = f = head
            count = 1
            arr = []
            while f.next and f.next.next:
                arr.append(s.val)
                s = s.next #type: ignore
                f = f.next.next
                count+=2
            
            if f.next:
                f = f.next
                count+=1
            arr.append(s.val)
            
            right_node = None
            if count%2==0:
                s = s.next
                right_node = ListNode(s.val)
                
            while s.next:
                print(arr)
                left_node = ListNode(arr.pop(), right_node)
                right_node = ListNode(s.next.val,left_node)
                s = s.next
            
            head.next = right_node