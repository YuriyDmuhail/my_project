from logging import lastResort
from hb_logger import setup_logger
from datetime import datetime

def filter_heart_beat_log(key):
    filtered_heart_beat_log = []

    with open("hblog.txt", "r") as file:
        for line in file.readlines():
            if key in line.strip():
                filtered_heart_beat_log.append(line)
    print(filtered_heart_beat_log)

    return filtered_heart_beat_log


def analyze_filtered_heart_beat_log(filtered_heart_beat_log):
    logger = setup_logger()
    time_stamps = []
    for line in filtered_heart_beat_log:
        if "Timestamp" in line:
            parts = line.split()
            time_str = parts[parts.index("Timestamp") + 1]
            time_stamps.append(datetime.strptime(time_str, "%H:%M:%S"))

    for i in range(len(time_stamps)-1):
        delta = (time_stamps[i] - time_stamps[i + 1]).total_seconds()
        if 31 < delta < 33:
            logger.warning(f"Heartbeat перевищує норму:{delta}. Початковий лог: {filtered_heart_beat_log[i]} Кінцевий лог:{filtered_heart_beat_log[i+1]}")
        elif delta >= 33:
            logger.error(f"Heartbeat перевищує норму:{delta}. Початковий лог: {filtered_heart_beat_log[i]} Кінцевий лог:{filtered_heart_beat_log[i+1]}")









#"Key TSTFEED0300|7E3E|0400"
analyze_filtered_heart_beat_log(filter_heart_beat_log("TSTFEED0300|7E3E|0400"))






