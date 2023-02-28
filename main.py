from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from decouple import config


def login(driver, password):
    """Login into IDMS"""
    print('Logging into IDMS...')
    send_password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "password")))
    send_password.send_keys(password)
    login = driver.find_element(By.ID, "next")
    login.click()

    # Enter the 2FA code manually
    send_2fa_button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, "phoneVerificationControl-readOnly_but_send_code")))
    send_2fa_button.click()
    auth_code = input('Please enter the 2FA code: ')
    send_2fa_code = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "verificationCode")))
    send_2fa_code.send_keys(auth_code)
    send_2fa_button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, "phoneVerificationControl-readOnly_but_verify_code")))
    send_2fa_button.click()


if __name__ == '__main__':
    username = config('USER')
    password = config('PASSWORD')
    url = config('URL')
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)
    login(driver, password)
