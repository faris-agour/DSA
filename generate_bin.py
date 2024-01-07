from queue import Queue

q = Queue()
n = int(input("convert into binary numbers from 1 to : "))
q.enqueue("1")

while n > 0:
    res = q.front()
    q.dequeue()

    res1 = res + '0'
    res2 = res + '1'

    q.enqueue(res1)
    q.enqueue(res2)

    print(res)

    n -= 1
