from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Test.configuration import *
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class MainPage:
    """
    Базовый класс для всех страниц.
    Содержит общие методы для работы с элементами на странице, такие как клик и ввод текста.
    """
    def __init__(self, driver):
        """
        Инициализация базовой страницы.
        :param driver: объект веб-драйвера Selenium.
        """
        self.driver = driver

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def test_buy_book(chrome_browser):
        chrome_browser.get(URL_1)

        chrome_browser.find_element(By.CLASS_NAME, 'header-search__input').send_keys("Пушкин")

        chrome_browser.find_element(By.CLASS_NAME, 'header-search__button-icon').click()

        """Ожидание загрузки элемента""" 
        element = WebDriverWait(chrome_browser, 10).until( EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[1]/article[3]/a[1]/picture[1]/img[1]')) ) 
        """Скролл к элементу""" 
        chrome_browser.execute_script("arguments[0].scrollIntoView(true);", element) 

        """Клик по элементу""" 
        ActionChains(chrome_browser).move_to_element(element).click(element).perform()
        sleep(5)

        chrome_browser.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[6]/div[2]/div[1]/div[1]/div[2]/button[1]/div[1]/div[1]').click()
        sleep(5)

    def test_buy_book_verify(chrome_browser):
        chrome_browser.get(URL_1)
        """Поиск по Фамилии"""
        chrome_browser.find_element(By.CLASS_NAME, 'header-search__input').send_keys("Пушкин")

        """Клик по лупе"""
        chrome_browser.find_element(By.CLASS_NAME, 'header-search__button-icon').click()

        """Ожидание загрузки элемента """
        element = WebDriverWait(chrome_browser, 10).until( EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[1]/article[3]/a[1]/picture[1]/img[1]')))

        """Скролл к элементу""" 
        chrome_browser.execute_script("arguments[0].scrollIntoView(true);", element) 

        """Клик по элементу""" 
        ActionChains(chrome_browser).move_to_element(element).click(element).perform()
        sleep(5)

        """Закинуть в корзину"""
        chrome_browser.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[6]/div[2]/div[1]/div[1]/div[2]/button[1]/div[1]/div[1]').click()
        sleep(5)

        """Проверить товар в корзине"""
        chrome_browser.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[6]/div[2]/div[1]/div[1]/div[2]/button[1]/div[1]/div[1]').click()
        sleep(5)


    def test_book_delete(chrome_browser):
        chrome_browser.get(URL_1)
        """Поиск по фамилии"""
        chrome_browser.find_element(By.CLASS_NAME, 'header-search__input').send_keys("Пушкин")

        """Клик по лупе"""
        chrome_browser.find_element(By.CLASS_NAME, 'header-search__button-icon').click()

        """Ожидание загрузки элемента""" 
        element = WebDriverWait(chrome_browser, 10).until( EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[1]/article[3]/a[1]/picture[1]/img[1]')))

        """Скролл к элементу""" 
        chrome_browser.execute_script("arguments[0].scrollIntoView(true);", element) 

        """Клик по элементу""" 
        ActionChains(chrome_browser).move_to_element(element).click(element).perform()
        sleep(5)

        """Закинуть в корзину"""
        chrome_browser.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[6]/div[2]/div[1]/div[1]/div[2]/button[1]/div[1]/div[1]').click()
        sleep(5)

        """Проверить товар в корзине"""
        chrome_browser.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[6]/div[2]/div[1]/div[1]/div[2]/button[1]/div[1]/div[1]').click()
        sleep(5)

        """Удалить из корзины"""
        chrome_browser.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/span[1]').click()
        sleep(5)

    def test_cart_recovery(chrome_browser):
        chrome_browser.get(URL_1)
        """Поиск по фамилии автора"""
        chrome_browser.find_element(By.CLASS_NAME, 'header-search__input').send_keys("Пушкин")

        """Клик по лупе"""
        chrome_browser.find_element(By.CLASS_NAME, 'header-search__button-icon').click()

        """Ожидание загрузки элемента"""
        element = WebDriverWait(chrome_browser, 10).until( EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[1]/article[3]/a[1]/picture[1]/img[1]')))

        """Скролл к элементу""" 
        chrome_browser.execute_script("arguments[0].scrollIntoView(true);", element) 

        """Клик по элементу""" 
        ActionChains(chrome_browser).move_to_element(element).click(element).perform()
        sleep(5)

        """Закинуть в корзину"""
        chrome_browser.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[6]/div[2]/div[1]/div[1]/div[2]/button[1]/div[1]/div[1]').click()
        sleep(5)

        """Проверить товар в корзине"""
        chrome_browser.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[6]/div[2]/div[1]/div[1]/div[2]/button[1]/div[1]/div[1]').click()
        sleep(5)

        """Удалить из корзины"""
        chrome_browser.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/span[1]').click()
        sleep(5)

        """Востановить корзину"""
        chrome_browser.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/section[1]/div[1]/div[2]').click()
        sleep(5)

    def test_book_placing(chrome_browser):
        chrome_browser.get(URL_1)
        """Поиск по фамилии автора"""
        chrome_browser.find_element(By.CLASS_NAME, 'header-search__input').send_keys("Пушкин")

        """Клик по лупе"""
        chrome_browser.find_element(By.CLASS_NAME, 'header-search__button-icon').click()

        """Ожидание загрузки элемента""" 
        element = WebDriverWait(chrome_browser, 10).until( EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[1]/article[3]/a[1]/picture[1]/img[1]')))

        """Скролл к элементу""" 
        chrome_browser.execute_script("arguments[0].scrollIntoView(true);", element) 

        """Клик по элементу""" 
        ActionChains(chrome_browser).move_to_element(element).click(element).perform()
        sleep(5)

        """Закинуть в корзину"""
        chrome_browser.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[6]/div[2]/div[1]/div[1]/div[2]/button[1]/div[1]/div[1]').click()
        sleep(5)

        """Проверить товар в корзине"""
        chrome_browser.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[6]/div[2]/div[1]/div[1]/div[2]/button[1]/div[1]/div[1]').click()
        sleep(5)

        """Удалить из корзины"""
        chrome_browser.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/span[1]').click()
        sleep(5)

        """Востановить корзину"""
        chrome_browser.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/section[1]/div[1]/div[2]').click()
        sleep(5)

        """Перейти к оформлению и ожидание загрузки элемента""" 
        element = WebDriverWait(chrome_browser, 10).until( EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div[2]/section[3]/button[1]')))

        """Скролл к элементу""" 
        chrome_browser.execute_script("arguments[0].scrollIntoView(true);", element) 

        """Клик по элементу"""
        ActionChains(chrome_browser).move_to_element(element).click(element).perform()
        sleep(5)