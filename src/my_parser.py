import requests
from bs4 import BeautifulSoup

persones = []
persone = {
    'city': '',
    'name': '',
    'position': '',
    'email': '',
}

def get_accept_website(url: str)->requests.models.Response:
    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        'Upgrade-Insecure-Requests': '1',
    }
    session = requests.Session()
    request = session.get(url, headers=headers)
    return request

def get_html_doc(my_url: str)->BeautifulSoup:
    with get_accept_website(my_url) as session:
        root = BeautifulSoup(session.text, 'html.parser')
    return root

def get_name(html_doc: BeautifulSoup):
    name = ''
    quites = html_doc.find_all('div', class_='t396__elem')
    return quites

def parse(my_url: str):
    html_doc = get_html_doc(my_url)
    print(get_name(html_doc))


if __name__=='__main__':
    my_url = 'https://mediakit-portals.shkulevholding.ru/our-team'
    parse(my_url)