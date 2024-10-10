import pytest
import allure
from Test.configuration import token
from Pages.page_api import ChitaiGorodAPI


@allure.step("Изменить личные данные с неверным токеном")
def test_update_personal_data_negative(chrome_browser):
    api = ChitaiGorodAPI("Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIxMDg2NjYwLCJpYXQiOjE3Mjc4ODYxNDYsImV4cCI6MTcyNzg4OTc0NiwidHlwZSI6MjB9.UIk1tIBDZULsvhqVL6yJ5l8L0w75fScZA3Cka_3EZFQ")
    data = {
        "lastName": "Васильева",
        "firstName": "ЭльвираЛ",
        "middleName": "",
        "birthday": "1988-06-30",
        "phone": "79091371749",
        "email": "elviraloskutova8@gmail.com",
        "phoneCountry": ""
        }

    response = api.update_personal_data(data)
    assert response.status_code == 401, "Status code should be 401"

@allure.step("Изменить личные данные с верным токеном")
def test_update_personal_data_positive(chrome_browser):
    api = ChitaiGorodAPI(token)
    data = {
        "lastName": "Васильева",
        "firstName": "ЭльвираЛ",
        "middleName": "",
        "birthday": "1988-06-30",
        "phone": "79091371749",
        "email": "elviraloskutova8@gmail.com",
        "phoneCountry": ""
        }

    response = api.update_personal_data(data)
    assert response.status_code == 200, "Status code should be 200 OK"

@allure.step("Поиск книг по автору")
def test_search_author(chrome_browser):
    api = ChitaiGorodAPI(token)
    response = api.search_author("пушкин", 2463)
    assert response.status_code == 204, "Status code should be 204 OK"

@allure.step("Добавление товара в корзину")
def test_add_basket(chrome_browser):
    api = ChitaiGorodAPI(token)
    ad_data = {"item_list_name": "search", "product_shelf": ""}
    response = api.add_to_basket(2886336, ad_data)
    assert response.status_code == 200, "Status code should be 200 OK"

@allure.step("Очищение корзины")
def test_clear_basket(chrome_browser):
    api = ChitaiGorodAPI(token)
    response = api.clear_basket()
    assert response.status_code == 204, "Status code should be 204 OK"