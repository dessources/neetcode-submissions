class ListNode:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.len = 0
        self.cap = capacity
        self.hm = {}                  
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.hm:
            value, node = self.hm[key]
            self._remove(node)
            self._insert(node)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            _, node = self.hm[key]
            self._remove(node)
            self._insert(node)
            self.hm[key] = (value, node)
        else:
            if self.len == self.cap:
                del self.hm[self.head.next.val]
                self._remove(self.head.next)
            else:
                self.len +=1
                
            node = ListNode(key)
            self._insert(node)
            self.hm[key] = (value, node)
                
                
    def _insert(self, node: ListNode) -> None:
        temp = self.tail.prev
        self.tail.prev = node
        temp.next = node
        node.next = self.tail
        node.prev = temp
    
    def _remove(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev