import requests
from bs4 import BeautifulSoup


class Quote:
    def __init__(self) -> None:
        pass

    def get_current_quote(self, currency: str, exchange: str) -> str:
        """
        Gets current quote for intended currency and exchange.

        Example for bitcoin as currency and brazilian real as
        exchange:

        currency: 'btc'
        exchange: 'brl'
        """
        self.currency = currency
        self.exchange = exchange
        url = f'https://www.google.com/finance/quote/{self.currency}-{self.exchange}'

        try:
            response = requests.get(url)
            response.raise_for_status()
            # Parse html
            soup = BeautifulSoup(response.content, 'html.parser')
            # Find current exchange
            current_price = soup.find('div', class_='YMlKec fxKbKc').text
        except requests.exceptions.HTTPError as errh:
            print('Http Error:', errh)
        except requests.exceptions.ConnectionError as errc:
            print('Error Connecting:', errc)
        except requests.exceptions.Timeout as errt:
            print('Timeout Error:', errt)
        except requests.exceptions.RequestException as err:
            print('Request failed', err)
        return current_price
