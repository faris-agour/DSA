class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        node = Node(value)
        self.top = node
        self.length = 1

    def push(self, value):
        node = Node(value)
        if self.length == 0:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.length += 1
        return True

    def pop(self):
        temp = self.top
        if self.length == 0:
            return None

        if self.length == 1:
            self.top = None
            self.length -= 1
            return temp

        self.top = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next


stack = Stack(2)

stack.push(4)
stack.push(6)

stack.pop()

# stack.pop()  
stack.print_stack()
print('----------')

print(stack.top.value)
