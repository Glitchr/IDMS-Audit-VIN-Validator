from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def inventory_button(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[4]/ul/li[2]/a")))
    
    def click_inventory_button(self):
        self.inventory_button.click()    

    @property
    def status_dropdown(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.ID, "StatusDisplay")))
    
    def change_status(self):
        self.status_dropdown.click()
        status0 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "Status0")))
        status0.click()

    def wait_for_loading_screen(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "spinnerContent")))
    
    def get_search_input(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[1]/div[5]/form/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div/input")))
       
    def enter_vin(self, vin):
        self.wait_for_loading_screen()
        search_inventory = self.get_search_input()
        search_inventory.clear()
        search_inventory.send_keys(vin)
        search_button = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div[1]/div[4]/div[2]/button")
        search_button.click()
    
    def get_response(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "totalRecordsFound")))            
            return True  # if the element is found, return True
        
        except TimeoutException:            
            return False  # if the element is not found, return False
