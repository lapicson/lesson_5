# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_vocabulare = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_num_list = []
with open('numbers.txt', 'r') as num_file:
    for data in num_file:
        data = data.split(' ', 1)
        my_num_list.append(my_vocabulare[data[0]] + ' ' + data[1])
    print(num_file)

with open('numbers_next.txt', 'w') as next_num_file:
    next_num_file.writelines(my_num_list)