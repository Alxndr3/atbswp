def print_table(list_):
    string_len = 0
    for i in range(len(list_[0])):
        for j in range(len(list_)):
            if string_len < len(list_[j][i]):
                string_len = len(list_[j][i])
    for i in range(len(list_[0])):
        for j in range(len(list_)):
            print(list_[j][i].rjust(string_len), end=' ')
        print()

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


print_table(table_data)
