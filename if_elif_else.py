# age = int(input(" ваш возраст: "))
# money = int(input(" ваш бюджет: "))
# if age < 18:
#     print('вам еще рано!')
# if money < 1000:
#     print('sorry f*ck u')
# elif money > 999:
#     print('welcome govnuk')
# elif age >= 18 and age < 21:
#     print('welcome!')
#     print('вам подходит сок')
# elif age >= 21:
#     print('алкоголь можно')
# elif age > 100 or age < 0:
#     print('не правильный возраст!')

# 1 Создайте 2 переменные со значениями 2**3 и 3**2 и покажите значение переменной в которой значение больше.


# a = 2**3
# b = 3**2
# if a > b:
#     print('its a')
# else:
#     print('its b')


# 2 У нас есть числа от 0 до 100, но не все числа разрешены!
# Разрешенённые: От 0 до 21 От 57 до 100 Как узнать что какое-то число из запрещёного диапазона?


# number = int(input('your number: '))
# if number >= 0 and number <= 21:
#     print("access")
# elif number >= 57 and number <= 100:
#     print("access")
# else:
#     print("error")


# Написать программу которая проверит число на несколько критериев:
# Чётное ли число?
# Делится ли число на 3 без остатка?
# Если возвести его в квадрат, больше ли оно 1000?

# number = int(input('your number: '))
#
# if number % 2 == 0:
#     print(f'{number} четное число')
# else:
#     print(f'{number} не четное число')
# if number % 3 == 0:
#     print(f'{number} число делится на 3 без отсатка')
# else:
#     print(f'{number} число не делится на 3 без отсатка')
# if number ** 2 < 1000:
#     print(f'квадрат {number} меньше чем 1000')
# else:
#     print(f'квадрат {number} больше чем 1000')

# 4 Создайте условие которое будет срабатывать в любом случае.

# name = input('write password: ')
# if len(name) < 100:
#     print('слишком короткий пороль!')
# else:
#     print('молодец!')

# 5 У вас есть переменная а=10//5 и b=10/5
# Ровны ли переменные a и b?
# если они равны выведите  их сумму

# a = 10 // 5
# b = 10 / 5
# if a == b:
#     print(True)
#     print(a + b)
# else:
#     print(False)

# Problem 6: Напишите условие, которое выводит отрицательные числа

# number = int(input('могу сделать любое число отрицательным: '))
# if number < 0:
#     print(f'{number} число итак отрицательное')
# else:
#     number *= -1
#     print(f"{number} теперь отрицптельное число")

# Problem 7:
# У вас есть переменные a=10 и b=5
# Напишите условие которое проверяет, являются ли ваши переменные положительными числами(только один if)
# a = 10
# b = 5
# if a > 0 and b > 0:
#     print(True)
# else:
#     print(False)

# Problem 8:
# Для переменных из прошлого задания(7) напишите условие которые выясняет, a больше b, если это так, то выведите a+2
# Иначе, b+2

# a = 10
# b = 5
# if a > b:
#     print(True)
#     print(a + 2)
# else:
#     print(False)
#     print(b + 2)


# Problem 9:
# Запросить у пользователя ввести любое число и если это число больше 0 вывести сообщение "Положительное число",
# если меньше 0 вывести сообщение "Отрицательное число" иначе вывести само число

# number = int(input('your number: '))
#
# if number > 0:
#     print(f'{number} Положительное число')
# elif number < 0:
#     print(f'{number} Отрицательное число')
# else:
#     print(number)

# Problem 10:
# Спросить у пользователя его возраст, если значение больше или равно 18 вывести сообщение "Совершеннолетний",
# если меньше или равно 4 вывести "Ребенок" иначе "Несовершеннолетий"

# age = int(input(" ваш возраст: "))
# if age >= 18:
#     print('Совершеннолетний')
# elif age <= 4:
#     print('Ребенок')
# else:
#     print('Несовершеннолетий')

# Problem 11:
# Создайте 2 переменные со значениями 45 и 6,
# проверить делится ли первое число на второе, если делится вывести соответствующее сообщение
# a = 45
# b = 6
# if a % b == 0:
#     print(True)
# else:
#     print(False)

# Problem 12:
# Написать программу где надо ввести любой год и вывести сообщение "Текущий год" если это текущий год,
# если будущий год вывести "Год еще не наступил" иначе "Год прошел"

# year = int(input('введите год'))
# if year == 2022:
#     print('Текущий год')
# elif year < 2022:
#     print('Год прошел')
# elif year > 2022:
#     print('Год еще не наступил')

# Problem 13:
# Спросить у пользователя его год рождения,вычислить  его возраст,
# если  возраст больше или равно 18 вывести сообщение "Совершеннолетний",
# если меньше или равно 4 вывести "Ребенок" иначе "Несовершеннолетий"

# year = int(input(" год рождения: "))
# age = 2022 - year
# if age >= 18:
#     print('Совершеннолетний')
# elif age <= 4:
#     print('Ребенок')
# else:
#     print('Несовершеннолетий')

# Problem 14:
# Создайте условие которое определит самое большое и самое маленькое число из трёх.
# a = 1
# b = 3
# c = 2
# v = a,b,c
# print(max(v))

# Problem 15:
# Есть три числа 17391, 546, 934.
# Если каждое из них поделить на 17 по модулю, где остаток меньше всего?

# a = 17391
# b = 546
# c = 934
#
# a //= 17
# b //= 17
# c //= 17
#
# v = a, b, c
# print(min(v))


# Problem 16:
# Есть переменная  x = 13.
# Нужно возвести её в квадрат и сравнить с числом 172.
# Если x всё ещё меньше возвести в квадрат ещё раз.

# x = 13
# x = x ** 2
# if x < 172:
#     x = x ** 2
#     print(x)
# else:
#     pass