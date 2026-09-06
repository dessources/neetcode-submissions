class ListNode:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:
  
    def __init__(self, capacity: int):
        self.head, self.tail = ListNode(), ListNode()
        self.head.next, self.tail.prev = self.tail, self.head
        self.capacity = capacity
        self.hm = {}
        

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1
        node = self.hm[key]
        self._remove(node)
        self._insert(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            node = self.hm[key]
            node.val = value
            self._remove(node)
            self._insert(node)
        else:
            if len(self.hm) == self.capacity:
                lru = self.head.next
                del self.hm[lru.key]
                self._remove(lru)
            node = ListNode(key, value)
            self._insert(node)
            self.hm[key] = node
    
    def _insert(self, node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next , nxt.prev = nxt, prev
        
