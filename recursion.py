# ex/1 should return sum from num to 0

def rec_sum(num):
    return num + rec_sum(num - 1) if num != 0 else 0


print(rec_sum(5))  # 15

# ---------------------------------------------------------------------------------------
print('-' * 50)


# ex/2 should return sum of num individually

def sum_fun(num):
    return (num % 10) + sum_fun(num // 10) if num != 0 else 0


print(sum_fun(12345))  # 10

# ---------------------------------------------------------------------------------------
print('-' * 50)


# ex3 word split

def word_split(phrase, list_words, output=None):
    if output is None:
        output = []
    for w in list_words:
        if phrase.startswith(w):
            output.append(w)
            return word_split(phrase[len(w):], list_words, output)
    return output


print(word_split("helloandwelcomedad", ['hello', 'and', 'or', 'welcome', 'mom', 'dad']))

print('-' * 50)


# ---------------------------------------------------------------------------------------

# MEMOIZATION
# is an optimization technique used in programming to improve the performance of functions by caching
# (storing) the results of expensive function calls and returning the cached result when the same inputs occur again.

# use it in ex/1
def rec_sum_memo(num, memo={}):
    if num in memo:
        return f"Retrieved from cache: recursion_sum({num}) = {memo[num]}"
    if num == 0:
        return 0
    else:
        res = num + rec_sum(num - 1)
        memo[num] = res
        return res


print(rec_sum_memo(5))
print(rec_sum_memo(8))
print(rec_sum_memo(5))
print('-' * 50)


# ---------------------------------------------------------------------------------------
# reverse ex in rec
def reverse(s):
    # return s[::-1]
    # ==
    return reverse(s[1:]) + s[0] if len(s) >= 1 else s


print(reverse("fares"))

print('-' * 50)
# ---------------------------------------------------------------------------------------
# permutation
from itertools import permutations

input_string = '123'
perms = permutations(input_string)
l = []
for p in perms:
    a = ''.join(p)
    l.append(a)
print(l)
print('-' * 50)


# ---------------------------------------------------------------------------------------

# Fibonacci rec
def fibonacci(n):
    return fibonacci(n - 1) + fibonacci(n - 2) if n > 2 else 1


print(fibonacci(10))
