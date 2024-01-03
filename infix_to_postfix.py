class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, value):
        node = Node(value)
        if self.length == 0:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.length += 1
        return True

    def is_not_empty(self):
        return True if self.length > 0 else False

    def pop(self):
        if self.length == 0:
            return None

        temp = self.top
        self.top = temp.next
        self.length -= 1
        return temp.value


def HasHighPriority(top, operator):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    if top in precedence and operator in precedence:
        return precedence[top] >= precedence[operator]

    return False


s = Stack()
exp = input("Enter your infix expression: ")  # e.g., 2+3*(2-4)/8
op = ['+', '-', '/', '*', '^']
pt = ['(', ')']
new_exp = ''

for i in exp:
    if i not in op and i not in pt:
        new_exp += i
    elif i in op:
        while s.is_not_empty() and HasHighPriority(s.top.value, i) and s.top not in pt:
            new_exp += s.top.value
            s.pop()
        s.push(i)
    elif i == '(':
        s.push(i)

    elif i == ')':
        while s.is_not_empty() and s.top.value != '(':
            new_exp += s.top.value
            s.pop()
        s.pop()

while s.is_not_empty():
    new_exp += s.top.value
    s.pop()
print(new_exp)
