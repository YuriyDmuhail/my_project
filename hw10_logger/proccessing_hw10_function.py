from hw10_logger.homework_10 import log_event
def TakingLastLine():
    """
    Функція витягує останній запис з лог файл, і повертає user, status: str, user, status: str
    """
    with open("login_system.log", "r") as file:
        lines = file.readlines()
    if lines:
        last_log = lines[-1]  # Тут я витягую останній лог-рядок
        my_param = last_log.split(" - ")[-1] # Тут я роблю перший спліт і витягую останній блок - Username: Yuriy, Status: success
        user_status = my_param.split(", ") # роблю ще один спліт -['Username: Yuriy', 'Status: success']
        user = user_status[0].split(": ")[1].strip()  # Yuriy
        status = user_status[1].split(": ")[1].strip()  # success
        return user, status
    else:
        return None, None


