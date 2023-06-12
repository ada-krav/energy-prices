import sqlite3
import time

from datetime import date, timedelta

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


URL = "https://www.oree.com.ua/index.php/control/results_mo/DAM"
TOMORROW = date.today() + timedelta(days=1)


def market_is_closed(last_date):
    tomorrow = TOMORROW.strftime("%d.%m.%Y")
    return tomorrow == last_date


def is_date_in_database():
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT COUNT(*)
        FROM data
        WHERE date = ?
    ''', (TOMORROW,))

    count = cursor.fetchone()[0]

    conn.close()

    return count > 0


def get_clean_info(table):
    table_rows = table.find("tbody").find_all("tr")
    data = []
    for row in table_rows:
        columns = row.find_all("td")
        row_data = [column.get_text(strip=True) for column in columns]
        row_data[0] = TOMORROW
        data.append(row_data[0:-1])
    return data


def save_data(scraped_data):
    conn = sqlite3.connect("db.db")
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT INTO Data (date, hour, price, sales_volume, purchase_volume, declared_sales_volume, declared_purchase_volume) VALUES (?, ?, ?, ?, ?, ?, ?)",
        scraped_data,
    )

    conn.commit()
    conn.close()


def scrape_prices() -> None:
    driver = webdriver.Chrome()

    driver.get(URL)
    driver.implicitly_wait(100)

    element = driver.find_element(
        By.XPATH, "//*[contains(text(), 'Погодинні результати на РДН')]"
    )
    element.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "site-table"))
    )

    soup = BeautifulSoup(driver.page_source, "html.parser")
    last_date = soup.find("input", id="date_pxs").get("value")

    if is_date_in_database():
        exit(f"{TOMORROW} is already fetched")

    if market_is_closed(last_date):
        table = soup.select(".site-table")
        data = get_clean_info(table[0])
        save_data(data)

    else:
        driver.close()
        # script will be executed again and again till it gets data, currently once every 5 minutes
        time.sleep(300)
        scrape_prices()


scrape_prices()
