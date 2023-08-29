import requests
from bs4 import BeautifulSoup


def get_pages(link: str, blocks: str) -> list:
    """
    Function to send get requests and get pages elements
    You can stop parsing on statement (type and counter <= n)
    :param link: str
    :param blocks: str
    """
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    counter = 1
    base_url = link
    arr = []
    while True:
        req = requests.get(f'{base_url}{counter}', headers)
        if req.status_code == 200:
            print(f'Page {counter}')
            soup = BeautifulSoup(req.text, 'lxml')
            articles = soup.findAll('div', class_=blocks)
            arr += articles
            counter += 1
        else:
            break

    return arr
