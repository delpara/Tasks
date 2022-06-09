# Создаем список кубов чисел
list_3 = [i ** 3 for i in range(1, 1001) if i % 2 != 0]
print(list(list_3))

# Сумма чисел / 7
count = 0
for num in list_3:
    if sum(map(int, str(num))) % 7 == 0:
        count += num
print('Сумма чисел, сумма цифр которых / 7 = ', count)

# Добавить к каждому числу 17 и сделать п.2
new_count = 0
for num in list_3:
    num = num + 17
    if sum(map(int, str(num))) % 7 == 0:
        new_count += num
print('Новая сумма чисел, сумма цифр которых / 7 = ', new_count)
