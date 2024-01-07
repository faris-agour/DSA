def linear_search(my_list, value):
    for i in range(len(my_list)):
        if value == my_list[i]:
            return i  # return index of the value
    return -1


def bin_search(sorted_list, value):  # like bisection method in math5
    start = 0
    end = len(sorted_list) - 1
    while start <= end:
        value_index = (start + end) // 2
        if value == sorted_list[value_index]:
            return value_index
        elif value > sorted_list[value_index]:
            start = value_index + 1
        else:
            end = value_index - 1
    return -1


# print(linear_search([12, 33, 1, 7, 8, 44], 33))
print(bin_search([1, 11, 22, 31, 45, 88], 88))
# print(bin_search([1, 2], 1))
# print(bin_search([2, 3, 4, 5, 6, 7, 8, 9], 10))
