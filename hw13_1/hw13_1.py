import csv
from pathlib import Path

first_file = Path("Y:/py_teat_course/my_project/hw13_1/csv_files/random.csv")
second_file = Path("Y:/py_teat_course/my_project/hw13_1/csv_files/rmc.csv")

def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        return [row for row in reader]

data1 = read_csv(first_file)
data2 = read_csv(second_file)

combined_data = data1 + data2

#print(data1)

unique_data = []
seen = set()
for row in combined_data:
    row_tuple = tuple(row)
    if row_tuple not in seen:
        seen.add(row_tuple)
        unique_data.append(row)

# print(unique_data)
# print(seen)
def write_csv(file_path, data):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

result_file = Path("Y:/py_teat_course/my_project/hw13_1/csv_files/result_yuriy_file.csv")
write_csv(result_file, unique_data)