class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 增
    def append(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new

    # 删
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        cur = self.head
        while cur.next:
            if cur.next.data == data:
                cur.next = cur.next.next
                return
            cur = cur.next

    # 查
    def search(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return True
            cur = cur.next
        return False

    # 改
    def update(self, pos, new):
        if not self.head:
            return
        cur = self.head
        temp = 0
        while cur:
            if temp == pos:
                cur.data = new
                return
            cur = cur.next
            temp += 1

    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.append(2)
    linked_list.append(8)

    linked_list.display()

    linked_list.delete(2)
    linked_list.display()

    linked_list.update(1, 3)
    linked_list.display()

    print(linked_list.search(4))
    print(linked_list.search(3))
