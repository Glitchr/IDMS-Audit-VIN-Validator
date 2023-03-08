import csv

from selenium import webdriver
from decouple import config

from login_page import LoginPage
from inventory_page import InventoryPage


if __name__ == '__main__':
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

    # Open the read_file with all the info 
    # then write it into write_file once checked on IDMS
    with open('data/title_tec_temp_tags.csv', 'r') as read_file, \
    open('data/title_tec_temp_tags_updated.csv', 'w', newline='') as write_file:
        reader = csv.reader(read_file)
        writer = csv.writer(write_file)
        header = next(reader)
        writer.writerow(header)

        count = 1
        for row in reader:
            vin = row[1]
            inventory_page.enter_vin(vin)
            check_vin = inventory_page.check_vin_on_idms()

            print(f'\n({count}/1571) Vehicle S# {vin[-6:]}:')

            if check_vin:
                row[6] = 'x'
                print('\tAppears in IDMS')
            else:
                print('\tDoes not appear in IDMS')

            count += 1
            writer.writerow(row)

    print('\nFinished script')
    driver.quit()
