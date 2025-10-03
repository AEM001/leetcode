class MyLinkedList:

    def __init__(self):
        self.head=None

    def get(self, index: int) -> int:
        if index < 0 or not self.head:
            return -1
        cur = self.head
        count = 0
        while cur and count < index:
            count += 1
            cur = cur.next
        if cur:
            return cur.val
        return -1

            

    def addAtHead(self, val: int) -> None:
        newhead=Node(val)
        newhead.next=self.head
        self.head=newhead

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        newtail = Node(val)
        cur.next = newtail
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if not self.head:
            return
        cur = self.head
        count = 0
        while cur and count < index - 1:
            count += 1
            cur = cur.next
        if cur:
            newnode = Node(val)
            newnode.next = cur.next
            cur.next = newnode

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        cur = self.head
        count = 0
        while cur.next and count < index - 1:
            count += 1
            cur = cur.next
        if cur.next:
            cur.next = cur.next.next

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)