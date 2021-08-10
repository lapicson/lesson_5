# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open('hate_list.txt', 'r') as new_file:
    money = []
    miserable = []
    poverty_line = 20000
    new_file = new_file.read().split('\n')
    for data in new_file:
        data = data.split(' ')
        if int(data[1]) <= red_line:
            miserable.append(data[0])
        money.append(data[1])
    print('Персонажи-Мизерабли:', miserable)
    print('Средний доход на душу =', sum(map(int, money)) // len(money), 'рублей')
