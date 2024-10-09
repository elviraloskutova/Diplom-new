import requests
import pytest
from Test.configuration import token
import allure


@allure.step("Изменить личные данные с неверным токеном")
def test_update_personal_data_negative(chrome_browser):
    url = "https://web-gate.chitai-gorod.ru/api/v1/profile/personal-data"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7",
        "authorization": "token=Bearer%20eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIxMDg2NjYwLCJpYXQiOjE3Mjc4ODYxNDYsImV4cCI6MTcyNzg4OTc0NiwidHlwZSI6MjB9.UIk1tIBDZULsvhqVL6yJ5l8L0w75fScZA3Cka_3EZFQ",
        "content-type": "application/json",
        "origin": "https://www.chitai-gorod.ru",
        "referer": "https://www.chitai-gorod.ru/"
    }
    data = {
        "lastName": "Васильева",
        "firstName": "ЭльвираЛ",
        "middleName": "",
        "birthday": "1988-06-30",
        "phone": "79091371749",
        "email": "elviraloskutova8@gmail.com",
        "phoneCountry": ""
    }

    response = requests.patch(url, headers=headers, json=data)
    response_data = response.json()

    assert response.status_code == 401, "Status code should be 401"

@allure.step("Изменить личные данные с верным токеном")
def test_update_personal_data_positive(chrome_browser):
    url = "https://web-gate.chitai-gorod.ru/api/v1/profile/personal-data"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7",
        "authorization": token,
        "content-type": "application/json",
        "origin": "https://www.chitai-gorod.ru",
        "referer": "https://www.chitai-gorod.ru/"
    }
    data = {
        "lastName": "Васильева",
        "firstName": "ЭльвираЛ",
        "middleName": "",
        "birthday": "1988-06-30",
        "phone": "79091371749",
        "email": "elviraloskutova8@gmail.com",
        "phoneCountry": ""
    }

    response = requests.patch(url, headers=headers, json=data)
    response_data = response.json()

    assert response.status_code == 200, "Status code should be 200 OK"

@allure.step("Поиск книг по автору")
def test_search_author(chrome_browser):
    url = "https://web-gate.chitai-gorod.ru/api/v2/search/results"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7",
        "authorization": token,
        "content-type": "application/json",
        "origin": "https://www.chitai-gorod.ru",
        "referer": "https://www.chitai-gorod.ru/"
    }
    data = {
        "searchPhrase": "пушкин",
        "resultCount": 2463
    }

    response = requests.post(url, headers=headers, json=data)

    assert response.status_code == 204, "Status code should be 204 OK"

@allure.step("Изменить личные данные фамилии и имя")
def test_update_personal_data_positive(chrome_browser):
    url = "https://web-gate.chitai-gorod.ru/api/v1/profile/personal-data"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7",
        "authorization": token,
        "content-type": "application/json",
        "origin": "https://www.chitai-gorod.ru",
        "referer": "https://www.chitai-gorod.ru"
    }
    data = {
        "lastName": "Лоскутова",
        "firstName": "Эльвира",
        "middleName": "",
        "birthday": "1988-06-30",
        "phone": "79091371749",
        "email": "elviraloskutova8@gmail.com",
        "phoneCountry": ""
    }

    response = requests.patch(url, headers=headers, json=data)
    response_data = response.json()

    assert response.status_code == 200, "Status code should be 200 OK"

@allure.step("Добавление товара в корзину")
def test_add_basket(chrome_browser):
    url = "https://web-gate.chitai-gorod.ru/api/v1/cart/product"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7",
        "authorization": token,
        "content-type": "application/json",
        "origin": "https://www.chitai-gorod.ru",
        "referer": "https://www.chitai-gorod.ru/"
    }
    data = {
        "id": 2886336,
        "adData": {
            "item_list_name": "search",
            "product_shelf": ""
        }
    }

    response = requests.post(url, headers=headers, json=data)

    assert response.status_code == 200, "Status code should be 200 OK"

@allure.step("Очищение корзины")
def test_clear_basket(chrome_browser):
    url = "https://web-gate.chitai-gorod.ru/api/v1/cart"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7",
        "authorization": token,
        "content-type": "application/json",
        "origin": "https://www.chitai-gorod.ru",
        "referer": "https://www.chitai-gorod.ru/"
    }

    response = requests.delete(url, headers=headers)

    assert response.status_code == 204, "Status code should be 204 OK"