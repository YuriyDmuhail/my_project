# Напишіть декоратор, який логує аргументи та результати викликаної функції.


import functools
import datetime

def log_to_file(file_path='log.txt'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            try:
                result = func(*args, **kwargs)
                status = "SUCCESS"
                return result
            except Exception as e:
                result = f"Exception: {e}"
                status = "ERROR"
                raise
            finally:
                with open(file_path, 'a') as f:
                    f.write(f"[{datetime.datetime.now()}] "
                            f"Function: {func.__name__}\n"
                            f"Args: {args}, Kwargs: {kwargs}\n"
                            f"Status: {status}, Result: {result}\n"
                            f"{'-'*60}\n")
        return wrapper
    return decorator


@log_to_file()
def add(a, b):
    return a + b


add(3, 5)


# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
def exception_handl(some_function):
    def wrapper(*args, **kwargs):
        try:
            return some_function(*args, **kwargs)
        except Exception as e:
            print(f"Помилка у функції {some_function.__name__}: {e}")
            return None
    return wrapper

@exception_handl
def dvd(a, b):
    return a / b


print(dvd(10, 0))  # Виведе помилку, але не зламає програму
