import csv

from selenium import webdriver
from decouple import config
import pandas as pd

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
    read_csv = config('READ')
    write_csv = config('WRITE')
    df = pd.read_csv(read_csv)  # Read the CSV file into a dataframe
    df = df.fillna('')  # Turn any nan cells into empty strings
    row_count = len(df)  # Get the total number of rows
    with open(write_csv, 'w', newline='') as write_file:
        writer = csv.writer(write_file)
        header = df.columns  # Get the column names from the dataframe
        writer.writerow(header) 

        for index, row in df.iterrows():  # Iterate over each row in the dataframe
            index += 1
            vin = row['VIN']
            inventory_page.enter_vin(vin)
            result = inventory_page.check_vin_on_idms()

            print(f'\n({index}/{row_count}) Vehicle S# {vin[-6:]}:')

            if isinstance(result, bool):
                print('\tDoes not appear in IDMS')
            else:
                check_vin, year, make, model = result

                row['Year'] = year.text
                row['Make'] = make.text
                row['Model'] = model.text.partition('/')[0]
                row['VIN'] = vin[-6:]
                row['IDMS'] = 'x'
                print('\tAppears in IDMS')                   

            writer.writerow(row)  
    
    print('\nFinished script')
    driver.quit()
