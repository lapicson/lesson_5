# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open('my_file.txt', 'w') as new_file:

    while True:
        user_inp = input('Введите строку данных для файла: ')
        new_file.writelines(user_inp + '\n')
        new_file.flush()
        if user_inp == ' ':
            break
new_file.closed
print(new_file.closed)
