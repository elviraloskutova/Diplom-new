import requests

class ChitaiGorodAPI:
    base_url = "https://web-gate.chitai-gorod.ru"

    def __init__(self, token):
        self.headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7",
            "authorization": token,
            "content-type": "application/json",
            "origin": "https://www.chitai-gorod.ru",
            "referer": "https://www.chitai-gorod.ru/"
            }

    def update_personal_data(self, data):
        url = f"{self.base_url}/api/v1/profile/personal-data"
        response = requests.patch(url, headers=self.headers, json=data)
        return response

    def search_author(self, search_phrase, result_count):
        url = f"{self.base_url}/api/v2/search/results"
        data = {
            "searchPhrase": search_phrase,
            "resultCount": result_count
            }
        response = requests.post(url, headers=self.headers, json=data)
        return response

    def add_to_basket(self, product_id, ad_data):
        url = f"{self.base_url}/api/v1/cart/product"
        data = {
            "id": product_id,
            "adData": ad_data
            }
        response = requests.post(url, headers=self.headers, json=data)
        return response

    def clear_basket(self):
        url = f"{self.base_url}/api/v1/cart"
        response = requests.delete(url, headers=self.headers)
        return response