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
        hm = {None:None}
        temp = head
        while temp:
            hm[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        while temp:
            hm[temp].next = hm[temp.next]
            hm[temp].random = hm[temp.random]
            temp = temp.next
        
        return hm[head]