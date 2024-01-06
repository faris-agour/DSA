# First Sorting Algorithm
import time


def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list


def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list), 1):
            if my_list[min_index] > my_list[j]:
                min_index = j
        if min_index != i:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list


def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        j = i
        while my_list[j - 1] > my_list[j] and j > 0:
            my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
            j -= 1

    return my_list


def shell_sort(my_list):
    gap = len(my_list) // 2
    while gap > 0:
        for i in range(gap, len(my_list)):
            temp = my_list[i]
            j = i
            while j >= gap and my_list[j - gap] > temp:
                my_list[j] = my_list[j - gap]
                j -= gap
            my_list[j] = temp
        gap //= 2
    return my_list


# -----------------------------------------------
# a helper func
def merge(l1, l2):
    sorted_list = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] >= l2[j]:
            sorted_list.append(l2[j])
            j += 1
        else:
            sorted_list.append(l1[i])
            i += 1

    while i < len(l1):
        sorted_list.append(l1[i])
        i += 1
    while j < len(l2):
        sorted_list.append(l2[j])
        j += 1
    return sorted_list


def merge_sort(l):
    if len(l) == 1:
        return l
    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    return merge(left, right)


def get_pivot(l, start, end):
    pivot = start
    swap = start
    for i in range(start + 1, end):  # swap elements
        if l[pivot] > l[i]:  # here if l[1] is less also it will swap itself so that's ok
            swap += 1
            l[swap], l[i] = l[i], l[swap]
    l[swap], l[pivot] = l[pivot], l[swap]  # swap pivot
    return swap  # pivot that in the middle


def quick_sort(l, start=0, end=None):
    if end is None:
        end = len(l)

    if start < end:
        new_pivot = get_pivot(l, start, end)
        quick_sort(l, start, new_pivot)
        quick_sort(l, new_pivot + 1, end)
    return l


l = [3, 9, 2, 5, 90, 100, 12, 32, 43, 55, 9000, 86, 122, 34567, 989, 7, 22]

# print(bubble_sort(l))
# print(selection_sort(l))
# print(insertion_sort(l))
# print(shell_sort(l))

# print(merge_sort(l))
# print(quick_sort(l))

print(time.time())  # Record start time
print(quick_sort(l))
print(time.time())  # Record end time
