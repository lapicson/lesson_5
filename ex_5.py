# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open('my_num_file.txt', 'w') as new_file:
    user_input = input('Введите числа через пробел: ')
    new_file.write(user_input)
    new_file.close()
with open('my_num_file.txt', 'r') as file_sum:
    file_sum = file_sum.read().split(' ')
    summary_data = 0
    for data in file_sum:
        summary_data = summary_data + int(data)
print(summary_data)
