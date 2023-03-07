from selenium import webdriver
from decouple import config
from login_page import LoginPage


if __name__ == '__main__':
    username = config('USER')
    password = config('PASSWORD')
    url = config('URL')
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)
    login_page = LoginPage(driver)
    login_page.login(password)