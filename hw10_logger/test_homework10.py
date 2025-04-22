import pytest
from hw10_logger.proccessing_hw10_function import TakingLastLine
from hw10_logger.homework_10 import log_event

expected_statuses = ["success", "expired", "failed"]

class TestLoggingFile:
    def test_log_event_and_read(self): # Підготовка тестових даних
        """
        Базовий тест на відповідність останього рядка в лог файлі
        """
        username = "Yuriy"
        status = "success"
        log_event(username=username, status=status) # Викликаю функцію запису в лог файл
        result_user, result_status = TakingLastLine() # викликаю парсинг і записую в два параметра
        assert result_user == username
        assert status == result_status

    def test_log_event_wrong_status(self):
        """
        Перевірка на хибний статус
        """
        username = "NoMatter"
        status = "ex" # Хибний статус
        log_event(username=username, status=status)
        result_user, result_status = TakingLastLine()  # викликаю парсинг і записую в два параметра
        assert result_status not in expected_statuses

    def test_log_event_expected_statused(self):
        """
        Перевірка, що усі дозволені статуси записуються в лог файл
        """
        username = "NoMatter"
        for status in expected_statuses:
            log_event(username=username, status=status)
            result_user, result_status = TakingLastLine()  # викликаю парсинг і записую в два параметра
            assert result_status == status
            assert result_status in expected_statuses

    def test_log_event_without_name(self):
        """
        Перевірка на хибне ім'я
        """
        usernames = ["", None, 0]
        status = "success"
        for username in usernames:
            log_event(username=username, status=status)
            result_user, result_status = TakingLastLine()  # викликаю парсинг і записую в два параметра
            #але з цього тесту немає ніякого сенсу, бо функція не обробляє вхідні параметри
            assert result_user == str(username) or result_user == "None" or result_user == "0"