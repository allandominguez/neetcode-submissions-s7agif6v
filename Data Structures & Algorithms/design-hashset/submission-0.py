class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class MyHashSet:

    def __init__(self):
        self._set = [ListNode(-1) for _ in range(10**4)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            head = self._set[key % 10**4]
            node = ListNode(key)
            node.next = head.next
            head.next = node

    def remove(self, key: int) -> None:
        cur = self._set[key % 10**4]
        prev = None
        while cur:
            if cur.val == key:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next
        

    def contains(self, key: int) -> bool:
        cur = self._set[key % 10**4]
        while cur:
            if cur.val == key:
                return True
            cur = cur.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)