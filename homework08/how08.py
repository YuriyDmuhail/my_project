# Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
# [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”] ['21,57,88,10', 'qwerty,16,89,33,72', '6,95,58,44', '50,27,12,91,7', 'hello,31,47,8']
# Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
# Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”
# Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
# Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”

random_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
def sum_if_its_int(some_list):
    for row in some_list:
        try:
            sum = 0
            for i in row.split(','):
                sum += int(i)
            print(sum)
        # except TypeError:
        #     print('Не можу це зробити')
        except ValueError:
            print('Не можу це зробити')

sum_if_its_int(random_list)




