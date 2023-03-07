from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def password_field(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "password")))

    @property
    def next_button(self):
        return self.driver.find_element(By.ID, "next")

    @property
    def send_2fa_button(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.ID, "phoneVerificationControl-readOnly_but_send_code")))

    @property
    def verification_code_field(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, "verificationCode")))

    @property
    def verify_2fa_button(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.ID, "phoneVerificationControl-readOnly_but_verify_code")))

    def enter_password(self, password):
        self.password_field.send_keys(password)

    def click_next(self):
        self.next_button.click()

    def send_2fa_code(self):
        self.send_2fa_button.click()

    def enter_verification_code(self, code):
        self.verification_code_field.send_keys(code)

    def verify_2fa_code(self):
        self.verify_2fa_button.click()

    def login(self, password):
        self.enter_password(password)
        self.click_next()
        self.send_2fa_code()
        auth_code = input('Please enter the 2FA code: ')
        self.enter_verification_code(auth_code)
        self.verify_2fa_code()
