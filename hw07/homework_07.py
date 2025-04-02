# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
from os import strerror


def multiplication_table(number, maxResult):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier * number <= maxResult:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result >= maxResult:
            # Enter the action to take if the result is greater than 25
            pass
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3, 25)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def make_summ(x, y):
    print(x + y)

make_summ(2,3)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def everage_num (*some_list):
    result_everage_num = 0
    for i in some_list:
        result_everage_num +=i
    print(result_everage_num / len(some_list))

everage_num(1,2,3,4,5)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def oposit_str(your_str):
    print(your_str[::-1])

oposit_str("qwerty12345")
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def the_longest(some_list):
    len_of_list = [len(i) for i in some_list]
    indx_of_max_len = len_of_list.index(max(len_of_list))
    print(some_list[indx_of_max_len])

the_longest(['KwFaLbQ', 'xVjP', 'RstyZm', 'AhDgEk', 'plQrS111111'])

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 in str1:
        index = str1.index(str2[0])
        return index
    else:
        return -1


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
#Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
random_list = [42, 87, 23, 91, 56, 14, 68, 79, 35, 10, 99, 74, 62, 5, 31]

sum = 0

for i in random_list:
    if i % 2 == 0:
        sum += i

print(sum)


#Є list з даними . Напишіть код, який свормує новий list (наприклад lst2),
# який містить лише змінні типу стрінг, які присутні в lst1.
# Данні в лісті можуть бути будь якими

def list_with_str(lst):
    list_str_result = []
    for i in lst:
        if type(i) == str:
            list_str_result.append(i)
    print(list_str_result)


list_with_str(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'])

#Напишіть цикл, який буде вимагати від користувача ввести слово,
# в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

def give_me_h(my_str):
    lower_my_str = my_str.lower()
    while "h" not in lower_my_str:
        one_more_try = input("Введи ще раз:")
        return give_me_h(one_more_try)
    return print("дякую")



        #my_str = input("Введи слово, в якому буде хоч одна 'h' :")
        # find_h = my_str.lower()
        # if find_h.find("h") != -1:
        #     print("дякую")
        #     return True
        # else:
        #     one_more_try = input("Введи ще раз:")
        #     give_me_h(one_more_try)

give_me_h(input("Введи слово, в якому буде хоч одна 'h' :"))
#Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

def counting_uniqe(some_input):
    if len(set(some_input)) > 10:
        print(True)
    else:
        print(False)


counting_uniqe(input("Введи рандомний текст"))
