import json
import requests
import winsound
import pyperclip

import JsonQueries


class TradeController:
    def __init__(self, item_list):
        self.jsonQueries = JsonQueries.JsonQueries(item_list)
        self.frequency = 2500  # Set Frequency To 2500 Hertz
        self.duration = 600  # Set Duration To 1000 ms == 1 second

    def check_price(self, item, price):
        endpoint = "https://www.pathofexile.com/api/trade/search/harvest"
        query = self.jsonQueries.get_query(item)

        try:
            request = requests.post(url=endpoint, json=query)
            response_json = json.loads(request.text)
            item_codes = response_json["result"]
            response_id = response_json["id"]
            for item_code in item_codes:
                winsound.Beep(self.frequency, self.duration)
                url = "https://www.pathofexile.com/api/trade/fetch/" + item_code + "?query=" + response_id
                item_info_request = requests.get(url=url)
                item_info_response_json = json.loads(item_info_request.text)
                price = item_info_response_json["result"][0]["listing"]["price"]["amount"]
                currency = item_info_response_json["result"][0]["listing"]["price"]["currency"]
                message = item_info_response_json["result"][0]["listing"]["whisper"]
                seller = item_info_response_json["result"][0]["listing"]["account"]["name"]
                print(item + "  |  " + str(price) + " " + currency + "  |  " + seller + "  |  " + message)
                pyperclip.copy(message)
        except Exception as e:
            print("check_price exception: " + str(e))

