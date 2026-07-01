"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm = {}
        old = head
        new =curr = Node(0)
        
        while old:
            curr.next = hm[old] if old in hm else Node(old.val)
            curr = curr.next
            hm[old] = curr
            if old.random in hm:
                curr.random = hm[old.random]
            else: curr.random = Node(old.random.val) if old.random else None
                

            hm[old.random] = curr.random
            
            old  = old.next
        return new.next