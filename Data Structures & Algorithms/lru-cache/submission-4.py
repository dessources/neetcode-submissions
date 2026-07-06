
class ListNode:

    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hm = {}
        self.head, self.tail = ListNode(), ListNode()
        self.head.next, self.tail.prev = self.tail, self.head
        

    def get(self, key: int) -> int:
        if key in self.hm:
            node = self.hm[key]
            self._remove(node)
            self._insert(node)
            return node.val
        else: return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            node = self.hm[key]
            self._remove(node)
            self._insert(node)
            node.val = value
        else:
            if len(self.hm) == self.cap:
                lru = self.head.next
                del self.hm[lru.key]
                self.head = self.head.next
            node = ListNode(key, value)
            self._insert(node)
            self.hm[key] = node

    def _remove(self, node) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _insert(self, node) -> None:
        prev, nxt = self.tail.prev, self.tail
        node.next, node.prev = nxt, prev
        prev.next =nxt.prev = node

        
