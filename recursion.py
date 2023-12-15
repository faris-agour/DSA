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

