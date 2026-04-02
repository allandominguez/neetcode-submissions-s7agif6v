class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self):
        self._map = [ListNode(-1, -1) for _ in range(10**4)]

    def put(self, key: int, value: int) -> None:
        node = self._get_node(key)
        if node:
            node.val = value
            return
        head = self._map[key % 10**4]
        node = ListNode(key, value)
        node.next = head.next
        head.next = node
    
    def _get_node(self, key: int) -> Optional[ListNode]:
        cur = self._map[key % 10**4]
        while cur:
            if cur.key == key:
                return cur
            cur = cur.next
        return None

    def get(self, key: int) -> int:
        node = self._get_node(key)
        return node.val if node else -1

    def remove(self, key: int) -> None:
        cur = self._map[key % 10**4]
        prev = None
        while cur:
            if cur.key == key:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)