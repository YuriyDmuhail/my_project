import logging
from faker import Faker

# Вимикаємо дебаг-логи Faker
logging.getLogger("faker.factory").setLevel(logging.WARNING)

fake = Faker()

def get_user():
    return fake.name()


def get_int_to_20 ():
    return fake.random_int(1, 21)






