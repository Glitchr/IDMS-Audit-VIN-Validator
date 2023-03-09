from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class InventoryPage:

    def __init__(self, driver):
        """Initialize the selenium driver"""
        self.driver = driver

    @property
    def inventory_button(self):
        """Select the homepage's button to go to the inventory"""
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[4]/ul/li[2]/a")))
     
    @property
    def status_dropdown(self):
        """Select the Status dropdown from the page"""
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.ID, "StatusDisplay")))
    
    @property
    def get_search_input(self):
        """Select the search input field from the page"""
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[1]/div[5]/form/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div/input")))

    @property
    def waitout_loading_screen(self):
        """Wait for the loading screen to disappear"""
        return WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "spinnerContent")))
    
    @property
    def get_year(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="row_detail"]/td[2]/span')))
    
    @property
    def get_make(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="row_detail"]/td[3]/span')))
    
    @property
    def get_model(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="row_detail"]/td[4]/span')))

    def click_inventory_button(self):
        """Click the selected inventory button to go the inventory"""
        print('Navigate to the inventory') 
        self.inventory_button.click()    
    
    def change_status(self):
        """Change the value from Available to None from the status dropdown"""
        print('Changing the status from available to all')
        self.status_dropdown.click()
        status0 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "Status0")))
        status0.click()      
       
    def enter_vin(self, vin):
        """
        First check that there's no loading screen before continuing, then
        select the search field, clear it of values, enter the VIN then search
        if it appears registered in IDMS
        """
        self.waitout_loading_screen
        search_inventory = self.get_search_input
        search_inventory.clear()
        search_inventory.send_keys(vin)
        search_button = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div[1]/div[4]/div[2]/button")
        search_button.click()
    
    def check_vin_on_idms(self):
        """Check if the VIN exists on the IDMS inventory"""
        try: 
            self.waitout_loading_screen
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='_InventoryLookupFormElement']/div[2]/div[4]")))            
        except TimeoutException:
                return False
        else:            
            return True, self.get_year, self.get_make, self.get_model
