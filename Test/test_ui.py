import allure
from selenium.webdriver.common.by import By
from Pages.page_ui import BookPage
from Test.configuration import URL_1


@allure.step("Положить книгу в корзину")
def test_buy_book(chrome_browser):
    book_page = BookPage(chrome_browser)
    book_page.driver.get(URL_1)

    book_page.search_book("Пушкин")

    element = book_page.wait_for_element((By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[1]/article[3]/a[1]/picture[1]/img[1]'))
    book_page.scroll_to_element(element)
    book_page.click_element(element)

    book_page.add_book_to_cart()


@allure.step("Проверить товар в корзине")
def test_buy_book_verify(chrome_browser):
    book_page = BookPage(chrome_browser)
    book_page.driver.get(URL_1)

    book_page.search_book("Пушкин")

    element = book_page.wait_for_element((By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[1]/article[3]/a[1]/picture[1]/img[1]'))
    book_page.scroll_to_element(element)
    book_page.click_element(element)

    book_page.add_book_to_cart()


@allure.step("Удаление книги из корзины")
def test_book_delete(chrome_browser):
    book_page = BookPage(chrome_browser)
    book_page.driver.get(URL_1)

    book_page.search_book("Пушкин")

    # Ожидание и клик по элементу (книге)
    element = book_page.wait_for_element((By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[1]/article[3]/a[1]/picture[1]/img[1]'))
    book_page.scroll_to_element(element)
    book_page.click_element(element)

    # Добавление книги в корзину
    book_page.add_book_to_cart()

    # Клик по кнопке в шапке страницы для перехода в корзину
    cart_button = book_page.wait_for_element((By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/header[1]/div[1]/div[2]/a[1]/span[2]'))
    book_page.click_element(cart_button)

    # Удаление книги из корзины
    book_page.remove_book_from_cart()


@allure.step("Восстановление книги в корзине после удаления")
def test_cart_recovery(chrome_browser):
    book_page = BookPage(chrome_browser)
    book_page.driver.get(URL_1)

    book_page.search_book("Пушкин")

    element = book_page.wait_for_element((By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[1]/article[3]/a[1]/picture[1]/img[1]'))
    book_page.scroll_to_element(element)
    book_page.click_element(element)

    book_page.add_book_to_cart()

    # Клик по кнопке в шапке страницы для перехода в корзину
    cart_button = book_page.wait_for_element((By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/header[1]/div[1]/div[2]/a[1]/span[2]'))
    book_page.click_element(cart_button)

    book_page.remove_book_from_cart()
    book_page.restore_cart()


@allure.step("Оформление покупки книги")
def test_book_placing(chrome_browser):
    book_page = BookPage(chrome_browser)
    book_page.driver.get(URL_1)

    book_page.search_book("Пушкин")

    element = book_page.wait_for_element((By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[1]/article[3]/a[1]/picture[1]/img[1]'))
    book_page.scroll_to_element(element)
    book_page.click_element(element)

    book_page.add_book_to_cart()

    # Клик по кнопке в шапке страницы для перехода в корзину
    cart_button = book_page.wait_for_element((By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/header[1]/div[1]/div[2]/a[1]/span[2]'))
    book_page.click_element(cart_button)

    book_page.proceed_to_checkout()