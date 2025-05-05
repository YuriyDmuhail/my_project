import logging
import xml.etree.ElementTree as ET
from pathlib import Path

logging_xml_file = logging.getLogger("XmlLogger")
logging_xml_file.setLevel(logging.INFO)
handler = logging.FileHandler("something.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logging_xml_file.addHandler(handler)



# Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number
# і повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо
xml_path = Path("groups.xml")


def finding_incoming_value_from_xml(path):
    tree = ET.parse(path)
    root = tree.getroot()
    for child in root.findall("group"):
        number = child.find("number")
        if number is not None:
            incoming = child.find("timingExbytes/incoming")
            if incoming is not None:
                logging_xml_file.info(f"We`ve found {incoming.text}")


finding_incoming_value_from_xml(xml_path)

with open("something.log", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)