from stack import Stack

s1 = Stack()
c = input("Enter the expression: ")  # e.g., 23+1/2*3-
op = ['+', '-', '/', '*']

for i in c:
    if i not in op:
        s1.push(int(i))
    else:
        n2_node = s1.pop()
        n1_node = s1.pop()

        if n2_node is not None and n1_node is not None:
            n2 = n2_node
            n1 = n1_node

            if i == '+':
                res = n1 + n2
            elif i == '-':
                res = n1 - n2
            elif i == '*':
                res = n1 * n2
            else:
                res = n1 // n2
            s1.push(res)
        else:
            print("Invalid Operator..")
if s1.length > 1:
    print("----You Forgot An Operator----")
else:
    s1.print_stack()
