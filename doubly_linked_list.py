class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1
        return True

    def prepend(self, value):
        if self.length == 0:
            return self.append(value)

        node = Node(value)
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.length += 1
        return True

    def pop(self):

        if self.length == 0:
            return None

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return None

        temp = self.tail
        self.tail = temp.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1
        return temp

    def get(self, index):

        temp = self.head  # as default now

        if index < 0 or index >= self.length - 1:
            return None

        if index == 0:
            return temp

        if index == self.length - 1:
            temp = self.tail
            return temp

        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
            return temp

    def set(self, index, value):
        temp = self.get(index)
        temp.value = value
        if temp:
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        node = Node(value)
        temp = self.get(index - 1)
        node.next = temp.next
        temp.next.prev = node
        temp.next = node
        node.prev = temp
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        pre = self.get(index - 1)
        node = pre.next
        temp = node.next
        pre.next = temp
        node.next = None
        temp.prev = pre
        node.prev = None
        self.length -= 1
        return True

    def pop_first(self):
        if self.length == 0:
            return False
        if self.length == 1:
            return self.pop()
        temp = self.head
        self.head = temp.next
        self.head.prev = None
        temp.next = None
        self.length -= 1
        return temp

    def print_dll(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next


# dll = DoublyLinkedList(6)
# dll.append(7)
# dll.append(8)

# dll.pop()
# dll.pop()

# dll.prepend(5)

# dll.pop_first()

# get = dll.get(0)
# print(get.value)

# set = dll.set(0, 4)
# print(set)

# dll.insert(1, 6.5)

# dll.remove(2)

# dll.print_dll()
