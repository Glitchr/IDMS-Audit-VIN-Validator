import csv

from selenium import webdriver
from decouple import config

from login_page import LoginPage
from inventory_page import InventoryPage


if __name__ == '__main__':
    username = config('USER')
    password = config('PASSWORD')
    url = config('URL')
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)
    
    login_page = LoginPage(driver)
    login_page.login(password)

    inventory_page = InventoryPage(driver)
    inventory_page.click_inventory_button()
    inventory_page.change_status()

    with open('data/title_tec_temp_tags.csv', 'r') as read_file, open('data/title_tec_temp_tags_updated.csv', 'w', newline='') as write_file:
        reader = csv.reader(read_file)
        writer = csv.writer(write_file)
        header = next(reader)
        writer.writerow(header)

        for row in reader:
            vin = row[1]
            inventory_page.enter_vin(vin)
            response_message = inventory_page.get_response()

            if response_message:
                row[6] = 'x'
            writer.writerow(row)
    
    driver.quit()