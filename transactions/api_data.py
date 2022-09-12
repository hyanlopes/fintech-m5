import os

import dotenv
import requests

dotenv.load_dotenv()


class AssetTicketNotExist(KeyError):
    pass


class DataCrypto:
    @classmethod
    def get(cls, crypto="BTC"):
        url = f'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol={crypto}&market=BRL&interval=1min&apikey={os.getenv("API_KEY")}'

        try:
            r = requests.get(url)
            data = r.json()
            price_actual = [item for item in data["Time Series Crypto (1min)"].items()][
                0
            ]

            obj_for_api = {
                "information": data["Meta Data"],
                "date_quotation": price_actual[0],
                "price_actual": price_actual[1]["4. close"],
            }

            return obj_for_api
        except:
            raise AssetTicketNotExist(f"The {crypto} not exist in API database.")
