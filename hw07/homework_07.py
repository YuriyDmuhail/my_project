# task 1
def multiplication_table(number, maxResult):
    result_lines = []
    multiplier = 1
    while multiplier * number < maxResult:
        result = number * multiplier
        result_lines.append(f"{number}x{multiplier}={result}")
        multiplier += 1
    return result_lines


# task 2
def make_summ(x, y):
    return x + y


# task 3
def average_num(*some_list):
    return sum(some_list) / len(some_list)


# task 4
def opposite_str(your_str):
    return your_str[::-1]


# task 5
def the_longest(some_list):
    return max(some_list, key=len)


# task 6
def find_substring(str1, str2):
    if str2 in str1:
        return str1.index(str2)
    return -1


# task 10.1 — Сума всіх парних чисел
def sum_even_numbers(lst):
    return sum(i for i in lst if i % 2 == 0)


# task 10.2 — Тільки рядки зі списку
def list_with_str(lst):
    return [i for i in lst if isinstance(i, str)]


# task 10.3 — Перевірка на наявність 'h'
def give_me_h(my_str):
    while "h" not in my_str.lower():
        my_str = input("Введи ще раз: ")
    return "дякую"


# task 10.4 — Унікальні символи в строці
def counting_unique(some_input):
    return len(set(some_input)) > 10