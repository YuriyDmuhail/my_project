
# Реалізуйте ітератор для зворотного виведення елементів списку.

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


# for item in ReverseIterator([1, 2, 3, 4]):
#     print(item)

# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            if self.current % 2 == 0:
                value = self.current
                self.current += 1
                return value
            self.current += 1
        raise StopIteration


# for num in EvenIterator(10):
#     print(num)