def my_func(spam):
    new_spam = str()
    spam_len = len(spam)
    for i in range(spam_len):
        if i != spam_len - 1:
            new_spam += str(spam[i]) + ', '
        else:
            new_spam += 'and ' + spam[-1]
    return new_spam

my_list = ['eggs', 'rats', 3.1415, 'A']
print(my_func(my_list))