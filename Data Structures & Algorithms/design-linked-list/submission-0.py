class Node:
    def __init__(self, val): 
        self.val = val
        self.prev = None 
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.left = Node(0) 
        self.right = Node(0) 
        self.left.next = self.right 
        self.right.prev = self.left 

    def get(self, index: int) -> int:
        cur = self.left.next

        while cur and index > 0: 
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0: 
            return cur.val
        else:
            return -1 

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        next = self.left.next
        prev = self.left

        self.left.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def addAtTail(self, val: int) -> None:
        node = Node(val) 
        prev = self.right.prev
        next = self.right

        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while curr and index > 0: 
            index -= 1 
            curr = curr.next 
        if curr and index == 0:
            node = Node(val) 
            prev = curr.prev
            next = curr

            prev.next = node
            node.prev = prev
            node.next = curr
            curr.prev = node
        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index > 0: 
            index -= 1 
            curr = curr.next 
        if curr and curr != self.right and index == 0:
            prev = curr.prev
            next = curr.next

            prev.next = next
            next.prev = prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)