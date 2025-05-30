#Напишіть генератор, який повертає послідовність парних чисел від 0 до N.

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


# for num in even_numbers(10):
#     print(num)


#Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

# for num in fibonacci(20):
#     print(num)