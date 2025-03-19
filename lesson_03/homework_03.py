from itertools import count

alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = """
"Would you tell me, please, which way I ought to go from here?"\n
"That depends a good deal on where you want to get to," said the Cat.\n
"I don't much care where ——" said Alice.\n
"Then it doesn't matter which way you go," said the Cat.\n
"—— so long as I get somewhere," Alice added as an explanation.\n
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."
"""
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 4360402
azov_sea_area = 37800
sum_area = black_sea_area + azov_sea_area

print(f"Спільна площа морів: {sum_area}км2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total  = 375291
first_and_second_st = 250449
second_and_thrid_st = 222950

first_storage = total - second_and_thrid_st
second_storage = first_and_second_st - first_storage
third_storage = total - first_and_second_st

print(f"Перший склад має кількість: {first_storage}\nДругий склад має кількість: {second_storage}\nТретій склад має кількість: {third_storage}")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
installment_payment = 1.5
payment = 1179
total_sum = payment * (installment_payment * 12)

print(total_sum)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
Dano_numners = {"a": 8019, "d": 7248, "b": 9907, "e" : 7128, "c" :2789, "f": 19224}
Dano_dividers = {"a":8, "d" : 6, "b": 9, "e": 5,"c": 5, "f": 9}

for key  in Dano_numners:
    result = Dano_numners[key] % Dano_dividers[key]
    print(f"Остача {key} = {result}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

shop_list = { "l_pizza": {"count": 4,
                          "price": 274},
              "m_pizza": {"count": 2,
                          "price": 218},
              "juice": {"count": 4,
                          "price": 35},
              "cake": {"count": 1,
                          "price": 350},
              "water": {"count": 3,
                          "price": 21}
              }
total_summa = 0

for item in shop_list:
    counted = shop_list[item]["count"]
    priced = shop_list[item]["price"]
    on_counting = counted * priced
    total_summa += on_counting
print(f"Загальна сума = {total_summa}грн.")
# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos = 232
photos_per_page = 8
pages = photos // photos_per_page

if photos % photos_per_page == 0:
    print(f"Вистачить {pages} сторінок")
else:
    print(f"Потрібно {pages + 1} сторінок")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
bank = 48
fuel_consumption = 9

total_fuel = distance / 100 * fuel_consumption
total_stops = int(total_fuel) // bank

print(f"{total_fuel} літрів бензину знадобиться для такої подорожі")
print(f"{total_stops} щонайменше разів родині необхідно заїхати на заправку")