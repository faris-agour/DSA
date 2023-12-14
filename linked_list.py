class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def append(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def prepend(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if self.length == 0:
            return None

        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp.value

        else:
            new_tail = self.head
            while new_tail.next != self.tail:
                new_tail = new_tail.next
            temp = self.tail
            new_tail.next = None
            self.tail = new_tail
            self.length -= 1
            return temp.value

    def pop_first(self):
        temp = self.head
        if self.length == 0:
            return None

        elif self.length == 1:
            self.head = None
            self.tail = None
            return temp.value
        else:
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            return temp.value

    def get(self, index):
        temp = self.head
        if index < 0 or index >= self.length:
            return None
        else:
            for _ in range(index):
                temp = temp.next
            return temp

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        node = Node(value)

        if index < 0 or index > self.length:
            return False

        if index == 0:
            self.prepend(value)
            return True

        if index == self.length:
            self.append(value)
            return True

        temp = self.get(index - 1)
        node.next = temp.next
        temp.next = node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def reverse(self):
        if self.length == 0:
            return False
        if self.length == 1:
            return True

        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True


# my_linked_list = LinkedList(2)
# my_linked_list.append(3)
# my_linked_list.append(9)
#
# my_linked_list.append(12)
# my_linked_list.prepend(1)

# print(my_linked_list.pop())
# print(my_linked_list.pop_first())

# print(my_linked_list.get(0))
# my_linked_list.set(0, 1)

# my_linked_list.insert(0, 1)
# my_linked_list.insert(2, 6)
# my_linked_list.insert(4, 15)

# my_linked_list.remove(0)
# my_linked_list.remove(2)

# my_linked_list.reverse()

# my_linked_list.print_list()

