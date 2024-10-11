from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BookPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(30)  # Установка неявного ожидания (в секундах)

    def search_book(self, book_name):
        search_input = self.driver.find_element(By.CLASS_NAME, 'header-search__input')
        search_input.send_keys(book_name)
        search_button = self.driver.find_element(By.CLASS_NAME, 'header-search__button-icon')
        search_button.click()

    def wait_for_element(self, locator):
        # Используем явные ожидания для определенных случаев, где это необходимо
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_element(self, element):
        ActionChains(self.driver).move_to_element(element).click(element).perform()

    def add_book_to_cart(self):
        add_to_cart_button = self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[6]/div[2]/div[1]/div[1]/div[2]/button[1]/div[1]/div[1]')
        self.click_element(add_to_cart_button)

    def remove_book_from_cart(self):
        remove_button = self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/span[1]')
        self.click_element(remove_button)

    def restore_cart(self):
        restore_button = self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/section[1]/div[1]/div[2]')
        self.click_element(restore_button)

    def proceed_to_checkout(self):
        checkout_button = self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div[2]/section[3]/button[1]')
        self.scroll_to_element(checkout_button)
        self.click_element(checkout_button)