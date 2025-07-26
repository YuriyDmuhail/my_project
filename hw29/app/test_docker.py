import pytest
from app import db
import allure_pytest
import allure

@pytest.fixture(scope="session", autouse=True)
def setup_db():
    db.create_table()

@allure.feature("DB Docker")
class TestDocker:

    @allure.story("Insert and Select")
    def test_insert_and_fetch(self):

        with allure.step("Записати користувача"):
            db.insert_user("Alice", "alice@example.com")

        with allure.step("Робимо селект"):
            users = db.get_users()

        with allure.step("Перевірка чи записаний користувач є в базі"):
            assert any(u[1] == "Alice" for u in users)

    @allure.story("Update")
    def test_update(self):

        with allure.step("Записуєм користувача"):
            db.insert_user("Bob", "bob@example.com")

        with allure.step("Робимо селект"):
            users = db.get_users()

        with allure.step("Шукаємо ід користувача"):
            user_id = [u for u in users if u[1] == "Bob"][0][0]

        with allure.step("Оновити імʼя Bob -> Robert"):
            db.update_user(user_id, "Robert")

        with allure.step("Перевірити, що імʼя оновилось"):
            updated = [u for u in db.get_users() if u[0] == user_id][0]
            assert updated[1] == "Robert"

    @allure.story("Delete")
    def test_delete(self):
        with allure.step("Вставити Temp"):
            db.insert_user("Temp", "temp@example.com")

        with allure.step("Знайти його id"):
            users = db.get_users()
            user_id = [u for u in users if u[1] == "Temp"][0][0]

        with allure.step("Видалити користувача"):
            db.delete_user(user_id)

        with allure.step("Переконатися, що запису більше немає"):
            users = db.get_users()
            assert not any(u[0] == user_id for u in users)

    @allure.story("Failed")
    def test_failed(self):
        with allure.step("Тестове падіння тесту"):
            assert False
