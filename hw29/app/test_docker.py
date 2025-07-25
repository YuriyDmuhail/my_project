import pytest
from app import db

@pytest.fixture(scope="session", autouse=True)
def setup_db():
    db.create_table()

class TestDocker:

    def test_insert_and_fetch(self):
        db.insert_user("Alice", "alice@example.com")
        users = db.get_users()
        assert any(u[1] == "Alice" for u in users)

    def test_update(self):
        db.insert_user("Bob", "bob@example.com")
        users = db.get_users()  # ← без self
        user_id = [u for u in users if u[1] == "Bob"][0][0]
        db.update_user(user_id, "Robert")
        updated = [u for u in db.get_users() if u[0] == user_id][0]
        assert updated[1] == "Robert"

    def test_delete(self):
        db.insert_user("Temp", "temp@example.com")
        users = db.get_users()
        user_id = [u for u in users if u[1] == "Temp"][0][0]
        db.delete_user(user_id)
        users = db.get_users()
        assert not any(u[0] == user_id for u in users)


    def test_failed(self):
        assert False
