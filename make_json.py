import re
import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

id_data = []

def take_id():


    url = 'https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html'
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    list_items = soup.select('li')

    for item in list_items:
        item_id = item.get('data-product-id')
        if item_id != None:
            item_data = {
                "id": item_id,
                "name": item.text.strip()
            }
            id_data.append(item_data)


take_id()
print("take_id is done")
edge_driver_path = 'C:/Users/Archer/PycharmProjects/pythonProject_test_task/msedgedriver.exe'

service = Service(edge_driver_path)
options = Options()

def add_to_json(file_path, new_data):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if not isinstance(data, list):
                data = [data]
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(new_data)

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

driver = webdriver.Edge(service=service, options=options)
#with open('items.json', 'r', encoding='utf-8') as file:
data = id_data

for i in data:
    item_data = {}

    try:

        driver.get(f'https://www.mcdonalds.com/ua/uk-ua/product/{i["id"]}.html')
        item_data["Навза"] = i["name"]


        accordion_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "cmp-accordion__button"))
        )
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "cmp-product-details-main__right-rail"))
        )

        right_rail_text = driver.find_element(By.CLASS_NAME, "cmp-product-details-main__right-rail").text.strip()
        item_data["Опис"]= right_rail_text

        accordion_element.click()
        time.sleep(2)
        nutrition_info = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "cmp-nutrition-summary__heading-primary-item"))
        )
        nutrition_info2 = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "cmp-nutrition-summary__details-column-view-mobile"))
        )

        nutrient_values = {}
        for item in nutrition_info:
            key = item.find_element(By.CSS_SELECTOR, ".metric span:not(.sr-only)").text.strip()
            value = item.find_element(By.CSS_SELECTOR, ".value span:not(.sr-only)").text.strip()
            if key and key not in nutrient_values:
                nutrient_values[key] = value


        for key, value in nutrient_values.items():
            value += " " + re.search(r'\(([^)]+)\)', key).group(1)
            item_data[re.sub(r'\s*\([^)]*\)', '', key).strip()]= cleaned_text = value

        label_items = driver.find_elements(By.CSS_SELECTOR, "li.label-item")

        nutrient_values = {}
        for item in label_items:
            metric = item.find_element(By.CSS_SELECTOR, ".metric").text.strip()
            value = item.find_element(By.CSS_SELECTOR, ".value span:not(.sr-only)").text.strip()
            if metric not in nutrient_values:
                nutrient_values[metric] = value


        for key, value in nutrient_values.items():
            if key!='':
                item_data[key]= value

    except:
        print(f"Страница для продукта с id {i['id']} - {i['name']} не найдена.")
        continue

    add_to_json('desc.json', item_data)

print("json file is done")
driver.quit()